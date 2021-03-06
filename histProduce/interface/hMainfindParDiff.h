#ifndef __hMainfindParDiff_h__
#define __hMainfindParDiff_h__
#include "histProduce/histProduce/interface/hMain.h"

class histMain_findParDiff : public histMain
{
public:
    histMain_findParDiff ( TFileDirectory* d);
    virtual void Process( fwlite::Event* ev );
    virtual void Clear();
private:
    //enum dirName { fd020, fd025, fd030, fd035, fd040 };
    //enum dirName { fd1S = 1, fd2S, fd3S, fd4S, fd5S };
    enum dirName { pvtx000 = 0, pvtx005, pvtx010, pvtx015, pvtx020 };
    std::vector<myCut::generalCutList*> myCutLists;
    std::map< dirName, myCut::generalCutList*> testCuts;
    TFileDirectory* origDir;
    //virtual void createHisto( const std::string& name, dirName dName, int nbin, double min, double max ) ;
    //virtual void fillHisto( const std::string& name, dirName dName, double value ) ;
    virtual void specialClearHisto();
    std::map< dirName, std::map< std::string, TH1D* > > _hMap;
    std::map< dirName, std::string > _nMap;
    std::map< dirName, TFileDirectory > _dirMap;
};
#endif


