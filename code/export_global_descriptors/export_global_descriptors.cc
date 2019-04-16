/**********************************************************
This program will export all fisher vectors in an index to 
a text file
**********************************************************/

#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>

using namespace std;

void usage() {
    cout << "Export global descriptors to text file" << endl;
    cout << "Usage:" << endl;
    cout << "./export_global_descriptors --index[-i] gdindex_file --output[-o] output_base_path" << endl;
}

void readIndex(const string index_path, vector < vector < uint > >& word_descriptor) {
    int n_read; // aux. variable for reading

    // Open file for reading
    FILE* index_file = fopen(index_path.c_str(), "rb");
    if (index_file == NULL) {
        fprintf(stderr, "readIndex : Cannot open: %s\n", index_path.c_str());
        exit(EXIT_FAILURE);
    }

    // Get total size of file
    fseek(index_file, 0, SEEK_END);
    uint total_size_file = ftell(index_file);
    fseek(index_file, 0, SEEK_SET);

    // Read number of global descriptors
    int number_gd_to_read = 0;
    n_read = fread(&number_gd_to_read, sizeof(int), 1, index_file);

    // Infer number of gaussians from total size of file and number of global descriptors
    uint gd_number_gaussians = (total_size_file - sizeof(int)) / (number_gd_to_read * (2 * sizeof(float) + sizeof(int)));

    cout << "Index contains " << number_gd_to_read << " descriptors and was generated using " << gd_number_gaussians << " gaussians." << endl;

    // Allocate helper variables
    uint* word_descriptor_to_read = 
        new uint[gd_number_gaussians];

    word_descriptor.resize(number_gd_to_read);
    
    // Loop over items, read and insert them into word_descriptor
    for (int count_item = 0; 
         count_item < number_gd_to_read; 
         count_item++) {
        // Read data
        // NOTE: We ignore word_l1_norms and word_total_soft_assignment and
        // only extract the word_descriptor information.
        // We skip bytes corresponding to these values (one float per 
        // gaussian for each of them).
        fseek(index_file, 2*sizeof(float)*gd_number_gaussians, SEEK_CUR);
        n_read = fread(word_descriptor_to_read, sizeof(uint), 
                       gd_number_gaussians, index_file);

        word_descriptor.at(count_item)
            .resize(gd_number_gaussians);
        for (uint count_gaussian = 0; 
             count_gaussian < gd_number_gaussians; 
             count_gaussian++) {
            word_descriptor.at(count_item).at(count_gaussian)
                = word_descriptor_to_read[count_gaussian];
        }
    }

    // Clean up
    if (word_descriptor_to_read != NULL) {
        delete [] word_descriptor_to_read;
        word_descriptor_to_read = NULL;
    }

    // Close file
    fclose(index_file);
}

void read_and_export_global_descriptors(const string gdindex_path, const string output_file) {
    vector < vector < uint > > word_descriptor;
    readIndex(gdindex_path, word_descriptor);
    uint gd_number_gaussians = word_descriptor[0].size();
    
    string log_file_name = output_file;
    ofstream log_file_;
    log_file_.open(log_file_name.c_str());
        
    log_file_ << word_descriptor.size() << endl;
    log_file_ << gd_number_gaussians << endl;
    
    for(uint i=0; i<word_descriptor.size(); i++){
        for(uint j=0; j<gd_number_gaussians; j++){
            log_file_ << word_descriptor[i][j] << endl;
        }
    }
}

int main(int argc, char* * argv) {
    // Mandatory arguments
    string gdindex_path = "";
    string output_base_path = "";
    
    if (argc < 5) {
        cout << "Wrong usage!!!" << endl;
        cout << "***********************************" << endl;
        cout << "***********************************" << endl;
        cout << "***********************************" << endl;
        cout << "See usage below:" << endl;
        usage();
        exit(EXIT_FAILURE);
    } else {
        for (int count_arg = 1; count_arg < argc; count_arg++) {
            if ((!strcmp(argv[count_arg], "--index")) || (!strcmp(argv[count_arg], "-i"))) {
                gdindex_path = string(argv[count_arg + 1]);
                count_arg++;
            } else if ((!strcmp(argv[count_arg], "--output")) || (!strcmp(argv[count_arg], "-o"))) {
                output_base_path = string(argv[count_arg + 1]);
                count_arg++;
            } else {
                cout << "Unrecognized argument " << argv[count_arg] 
                     << " , quitting..." << endl;
                exit(EXIT_FAILURE);
            }
        }
    }

    cout << "Starting export using:" << endl;
    cout << "------>gdindex_path = " << gdindex_path  << endl;
    cout << "------>output_base_path = " << output_base_path  << endl;

    read_and_export_global_descriptors(gdindex_path, output_base_path);

    return EXIT_SUCCESS;
}
