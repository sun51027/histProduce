#ifndef __rooTHMainGenpnLbTk_h__
#define __rooTHMainGenpnLbTk_h__
#include "histProduce/histProduce/interface/rooTHMain.h"
#include "histProduce/histProduce/interface/formatTreepnLbTk.h"
#include "histProduce/histProduce/interface/usefulFuncs.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include <vector>
#include <utility> // std::pair

class root_TreeHistoMain_GenInfo_plusminus_LbTk : public root_TreeHistoMain, public formatTree_plusminus_LbTk
{
public:
    root_TreeHistoMain_GenInfo_plusminus_LbTk (TFileDirectory* d);
    virtual void Process( unsigned int pIdx ) override;
    virtual void RegTree() override;
    virtual void RegHisto() override;
    virtual void LoadSourceBranch() override;
    virtual void SummaryCalc() override;
private:
    const double kaonMass, protonMass, pionMass;

public:
    // if it is needed to add addiditional branch to new tree. added in this
    enum addVarD
    {
        originD = comNumD-1,
        totNumD
    };
    enum addVarI
    {
        originI = comNumI-1,
        pptonPID, pptonMomPID, pkaonPID, pkaonMomPID,
        nptonPID, nptonMomPID, nkaonPID, nkaonMomPID,
        totNumI
    };


    // store result of genetic algorithm, the values are written in constructor
    std::vector<double> gaRes;
};


#endif
