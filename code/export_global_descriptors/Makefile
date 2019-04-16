CXX=g++
CXXFLAGS = -std=c++0x -O3 -g -Wall -fmessage-length=0

PLATFORM=$(shell uname)
ifeq ($(PLATFORM),Darwin) # Mac options
else # Linux options
	CXXFLAGS += -fopenmp
endif

EXPORT_GD = export_global_descriptors

all: $(EXPORT_GD)

$(EXPORT_GD).o: $(EXPORT_GD).cc
	$(CXX) $(CXXFLAGS) -c $(EXPORT_GD).cc \
	-o $(EXPORT_GD).o

$(EXPORT_GD): $(EXPORT_GD).o 
	$(CXX) $(CXXFLAGS) \
	-o $(EXPORT_GD) $(EXPORT_GD).o

clean:
	rm -f $(EXPORT_GD) $(EXPORT_GD).o
