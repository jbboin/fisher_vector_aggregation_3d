#ifndef GDINDEX_H
#define GDINDEX_H

#include <string>
#include <vector>

#include "../../common/feature_set/feature_set.h"

extern "C" {
#include "../../common/yael_v260_modif/yael/gmm.h"
#include "../../common/yael_v260_modif/yael/vector.h"
}

using namespace std;

#ifndef PUSH_BIT
#define PUSH_BIT(packed, bit) \
  packed = packed << 1; \
  packed += bit;
#endif

#ifndef POWER_LAW
#define POWER_LAW(v, a, w)                        \
  w = (v >= 0) ? pow(v,a) : -1 * pow(-v,a);
#endif

#ifndef POWER_LAW_SAME
#define POWER_LAW_SAME(v, a)                        \
  v = (v >= 0) ? pow(v,a) : -1 * pow(-v,a);
#endif

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned short ushort;

// Default initializations for private variables
const uint LD_LENGTH_DEFAULT = 128;
const uint LD_FRAME_LENGTH_DEFAULT = 4;
const string LD_EXTENSION_DEFAULT = ".siftb";
const string LD_NAME_DEFAULT = "sift";
const float LD_PRE_PCA_POWER_DEFAULT = 0.5;
const uint GD_NUMBER_GAUSSIANS_DEFAULT = 512;
const float GD_POWER_DEFAULT = 0.5;
const bool GD_INTRA_NORMALIZATION_DEFAULT = false;
const bool GD_UNBINARIZED_DEFAULT = false;
const uint MIN_NUMBER_WORDS_SELECTED_DEFAULT = 20;
const int ASYM_SCORING_MODE_DEFAULT = 1; // default is ASYM_QAGS
const float SCORE_DEN_POWER_NORM_DEFAULT = 0.5;
const int WORD_SELECTION_MODE_DEFAULT = 0;
const float WORD_SELECTION_THRESH_DEFAULT = 7;

// Hamming distance above which score is just set to zero
const uint CORR_WEIGHTS_CLIPPING = 16;

// L2 norm sq thresh
const double L2_NORM_SQ_THRESH = 0.00001;

class GDIndex
{
 public:

  // Constructor
  GDIndex();

  // Destructor
  ~GDIndex();

  // Index I/O
  // -- write function that is used after indexing, writing 
  //    descriptors, l1 norms and total soft assignment information
  //    per Gaussian
  void write(const string index_path);
  // -- read function that will load index into index_ variables;
  //    if the index already contains items, it will append items to it.
  //    If both_sel_modes is false, this will load either L1 norms OR
  //    Total Soft Assignment information, depending on
  //    query_parameters_.word_selection_mode
  //    If both_sel_modes is true, this will load BOTH types of
  //    information.
  void read(const string index_path, const bool both_sel_modes = false);
  // -- This function writes a file useful in the case of using shots 
  //    with independent keyframes indexing
  void write_frame_list(const string file_path);

  // Clean variables in index_
  void clean_index();

  // Get number of stored global descriptors in index
  uint get_number_global_descriptors();

  // Generate index: these will populate index_
  // -- frame-based signatures
  void generate_index(const vector<string>& feature_files, 
                      const int verbose_level = 1);
  // -- shot/scene-based signatures
  void generate_index_shot_based(const vector<string>& feature_files, 
                                 const vector<uint>& shot_beg_frames,
                                 const int shot_mode, const int shot_keyf, 
                                 const int verbose_level = 1);
  // -- generate one global descriptor from features
  void generate_global_descriptor(const FeatureSet* feature_set, 
                                  vector<uint>& gd_word_descriptor, 
                                  vector<float>& gd_fv, 
                                  vector<float>& gd_word_l1_norm, 
                                  vector<float>& gd_word_total_soft_assignment);

  // Functions to generate point-indexed FV, index will be returned
  // by value
  void generate_point_index(const vector<string>& feature_files,
                            const int verbose_level,
                            vector < vector < uint > >& vec_feat_assgns,
                            vector < vector < float > >& vec_feat_assgn_weights,
                            vector < vector < vector < float > > >& vec_feat_residuals);
  // -- generate one point-indexed descriptor from features
  void generate_point_indexed_descriptor(const FeatureSet* feature_set,
                                         const int verbose_level,
                                         vector<uint>& feat_assgns,
                                         vector<float>& feat_assgn_weights,
                                         vector < vector < float > >& feat_residuals);

  // Query index from query's local descriptor path or pre-computed query global
  // descriptor (if using "query_index_ptr")
  void perform_query(const string local_descriptors_path, 
                     const GDIndex* query_index_ptr,
                     const uint query_number,
                     const vector<uint>& indices,
                     vector< pair<float,uint> >& results, 
                     const uint number_2nd_stage_rerank = 0,
                     GDIndex* gdindex_ptr_rerank = NULL,
                     const vector < vector < uint > >& group_lists_rerank
                       = vector < vector < uint > >(), 
                     const int verbose_level = 1);

  // Function to set index_parameters_
  void set_index_parameters(const uint ld_length, const uint ld_frame_length,
                            const string ld_extension, const string ld_name,
                            const uint ld_pca_dim, const float ld_pre_pca_power,
                            const uint gd_number_gaussians, const float gd_power,
                            const bool gd_intra_normalization,
                            const bool gd_unbinarized,
                            const string trained_parameters_path,
                            const int verbose_level = 1);

  // Function to set query_parameters_
  // -- Note that the correlation weights loaded here require that
  //    some of the index_parameters_ variables be set. So, ALWAYS
  //    load index_parameters_ BEFORE loading query_parameters_
  void set_query_parameters(const uint min_number_words_selected,
                            const int asym_scoring_mode,
                            const int word_selection_mode,
                            const float word_selection_thresh,
                            const float score_den_power_norm,
                            const string trained_parameters_path,
                            const int verbose_level = 1);

  /************ Public Constants *************/
  // Modes for shot detection
  enum {SHOT_MODE_INDEP_KEYF = 0, SHOT_MODE_SHOT_AGG = 1, SHOT_MODE_GLOBAL_AGG = 2, SHOT_MODE_TRACK_AGG = 3, SHOT_MODE_CUSTOM_AGG = 4};
  // Modes for local descriptor
  enum {SIFT_LOCAL_DESCRIPTOR = 0, SIFTGEO_LOCAL_DESCRIPTOR = 1};
  // Modes for asymmetric scoring
  enum {ASYM_OFF = 0, ASYM_QAGS = 1, ASYM_DAGS = 2, ASYM_SGS = 3};
  // SIFT constants
  enum {SIFT_LENGTH = 128, SIFTGEO_LENGTH = 128};
  enum {SIFT_FRAME_LENGTH = 4, SIFTGEO_FRAME_LENGTH = 9};
  static const string SIFT_EXTENSION;
  static const string SIFTGEO_EXTENSION;
  static const string SIFT_NAME;
  static const string SIFTGEO_NAME;
  // Other constants for now (we might turn them into options later)
  enum {LD_PCA_DIM = 32};
  
  /************ End of Public Constants *************/

 private:
  /************ Private Constants *************/
  // Mode used in word selection for querying
  enum {WORD_L1_NORM = 0, WORD_SOFT_ASSGN = 1};
  /************ End of Private Constants *************/

  /************ Variable  *************/  
  // Variables that will hold the index and number of signatures stored
  struct struct_index {
      // The index will contain, at any point, either Binarized FVs or FVs,
      // so only one of the two following variables will be used at a given
      // point, depending on index_parameters_.gd_unbinarized
      // By default, Binarized FVs are used
      vector < vector < uint > > word_descriptor; // Binarized FV
      vector < vector < float > > fv; // FV

      // Auxiliary word selection information
      vector < vector < float > > word_l1_norms;
      vector < vector < float > > word_total_soft_assignment;

      // Vector that keeps frame numbers that are actually indexed in the db,
      // used only when SHOT_MODE_INDEP_KEYF mode is used
      vector<uint> frame_numbers_in_db;

      // Number of global descriptors in database;
      // this variable is always updated in function update_index
      uint number_global_descriptors;

      // Variables which are used when scoring, holding values
      // for each database item; they are always updated in
      // function update_index()
      vector < uint > number_words_selected;
      vector < vector < float > > word_l2_norms_sq;
  };
  struct_index index_;

  // Index parameters
  struct struct_index_parameters {
      // Local descriptor information
      uint ld_length;
      uint ld_frame_length;
      string ld_extension;
      string ld_name;

      // Parameters for PCA-ing local descriptors
      uint ld_pca_dim; // this is set to a constant (32), such that the
               // binarized signature conveniently fits in a
               // 4-byte unsigned integer
      float ld_pre_pca_power;
      float* ld_mean_vector;
      vector<float*> ld_pca_eigenvectors;      

      // Parameters used for global descriptor computation
      gmm_t* gd_gmm;
      uint gd_number_gaussians;      
      float gd_power; // normalization factor if using SSR normalization
      bool gd_intra_normalization; // flag that sets IN normalization (instead
                                   // of SSR) -- in this case, gd_power is
                                   // unused
      bool gd_unbinarized; // flag that decides if using FV (true) or
                           // BFV (false). Default is false.
  };
  struct_index_parameters index_parameters_;

  // Variables relevant for query time
  struct struct_query_parameters {
      // -- Number of minimum words to require for matching
      uint min_number_words_selected;
      // -- Scoring mode (options: ASYM_OFF, ASYM_QAGS, ASYM_DAGS, ASYM_SGS)
      int asym_scoring_mode;
      // -- Type of word selection mode in use
      // WORD_L1_NORM: only globalWordL1Norm is used
      // WORD_SOFT_ASSGN: only globalWordTotalSoftAssignment is used
      int word_selection_mode;
      // -- Threshold to use in visual word selection (used in asymmetric mode)
      float word_selection_thresh;
      // -- Score denominator's power normalization
      float score_den_power_norm;
      // -- Parameters used in scoring
      float* fast_corr_weights;
      int pop_count[65536];
  };
  struct_query_parameters query_parameters_;

  /************ End of Variables  *************/

  /************ Functions *************/
  // Update index after additions or deletions to it
  void update_index();

  // Sign binarize residuals
  void sign_binarize(const vector<float>& gd_word_residuals, 
                     vector<uint>& gd_word_descriptor);

  // PCA projection for local descriptors
  void project_local_descriptor_pca(const float* desc, float* pca_desc);

  // This function samples the number_frames_out from the shot that begins at
  // frame first_frame and contains number_frames_this_shot, and returns the frame
  // indices in a sorted vector.
  // If one frame is requested (number_frames_out = 1), it will return the center one;
  // otherwise, it will try to take equally spaced frames; if this results in frames 
  // too concentrated at the beginning or the end, it will take only the center ones.
  void sample_frames_from_shot(const uint number_frames_out, 
                               const uint first_frame, 
                               const uint number_frames_this_shot, 
                               vector<uint>& out_frames);

  // Obtain score for database item, given a query descriptor
  void score_database_item(const vector<uint>& query_word_descriptor,
                           const vector<float>& query_fv,
                           const vector<float>& query_word_l1_norm,
                           const vector<float>& query_word_total_soft_assignment,
                           const vector<float>& query_word_l2_norm,
                           const uint db_ind,
                           float& score);

  // Query index with query global descriptor
  void query(const vector<uint>& query_word_descriptor,
             const vector<float>& query_fv,
             const vector<float>& query_word_l1_norm,
             const vector<float>& query_word_total_soft_assignment,
             const vector<uint>& database_indices,
             vector< pair<float,uint> >& database_scores_indices);

  // Query index with global descriptor in a second stage
  void query_2nd_stage(const vector<uint>& query_word_descriptor,
                       const vector<float>& query_fv,
                       const vector<float>& query_word_l1_norm,
                       const vector<float>& query_word_total_soft_assignment,
                       const uint number_2nd_stage_rerank,
                       const vector < vector < uint > >& group_lists_rerank,
                       const vector< pair<float,uint> >& first_stage_scores_indices,
                       vector< pair<float,uint> >& database_scores_indices);

  // Functions to load trained parameters from index_parameters_
  void load_ld_mean_vector(string path);
  void load_ld_pca_eigenvectors(string path);
  void load_gd_gmm(string path);

  // Functions to load trained parameters from query_parameters_
  void load_corr_weights(string path);

  // Helper function to compare pairs
  static bool cmp_float_uint_ascend(const pair<float,uint> pair1, 
                                    const pair<float,uint> pair2) {
      return pair1.first < pair2.first;
  }
  /************ End of Functions *************/


};

#endif
