#include "histProduce/histProduce/interface/tmainGenpnLbTk.h"
#include "histProduce/histProduce/interface/generalCutList.h"
#include "histProduce/histProduce/interface/fourMom.h"
#include "histProduce/histProduce/interface/usefulFuncs.h"
#include "DataFormats/GeometryVector/interface/GlobalVector.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "math.h"


treeMainGen_pnLbTk::treeMainGen_pnLbTk( TFileDirectory* d ) :
    treeMainGen( d, treeMain::Label("lbWriteSpecificDecay", "pL0BFitted", "bphAnalysis"), "pnLbTkGenInfo" ), formatTree_plusminus_LbTk( totNumD, totNumI ),
    kaonMass ( 0.493667 ), protonMass( 0.9382720813 ), pionMass( 0.13957061 ),
    antiCandLabel( treeMain::Label("lbWriteSpecificDecay", "nL0BFitted", "bphAnalysis"))
{
    RegTree();
}
void treeMainGen_pnLbTk::Process( fwlite::Event* ev )
{
    try
    {
        if ( !ev->isValid() ) return;
        GetByLabel( ev );

        // pv not recorded, use BS
        if ( !beamSpotHandle.isValid() ) return;
        const reco::BeamSpot& bs = *beamSpotHandle;

        std::vector<pat::CompositeCandidate>::const_iterator handleIter;
        std::vector<pat::CompositeCandidate>::const_iterator handleIend;
        // preselection for pCand {{{
        if ( !_handle.isValid() ) return;
        if ( _handle->size()  == 0 ) return;

        std::vector< std::pair< double, const pat::CompositeCandidate*> > candsSorted;
        candsSorted.clear();
        candsSorted.reserve( _handle->size() );
        handleIter = _handle->begin();
        handleIend = _handle->end  ();
        while( handleIter != handleIend )
        {
            const pat::CompositeCandidate& cand = *handleIter++;
            if ( !cand.hasUserFloat("fitMass") ) continue;
            if ( !cand.hasUserData("TkTk/Proton.fitMom") ) continue;
            if ( !cand.hasUserData(  "TkTk/Kaon.fitMom") ) continue;
            if ( !cand.hasUserFloat("TkTk/Proton.IPt") ) continue;
            if ( !cand.hasUserFloat(  "TkTk/Kaon.IPt") ) continue;
            if ( !cand.hasUserData( "fitVertex" ) ) continue;
            if ( !cand.hasUserData( "refToJPsi" ) ) continue;

            const GlobalVector* dPTR[2] = {nullptr};
            dPTR[0] = cand.userData<GlobalVector>("TkTk/Proton.fitMom");
            dPTR[1] = cand.userData<GlobalVector>("TkTk/Kaon.fitMom");

            const GlobalVector* muPTR[2] = {nullptr};
            muPTR[0] = cand.userData<GlobalVector>("JPsi/MuPos.fitMom");
            muPTR[1] = cand.userData<GlobalVector>("JPsi/MuNeg.fitMom");

            fourMom pMu ( muPTR[0]->x(), muPTR[0]->y(), muPTR[0]->z() );
            fourMom nMu ( muPTR[1]->x(), muPTR[1]->y(), muPTR[1]->z() );
            fourMom pTk ( dPTR[0]->x(), dPTR[0]->y(), dPTR[0]->z() );
            fourMom nTk ( dPTR[1]->x(), dPTR[1]->y(), dPTR[1]->z() );
            //fourMom tktk = pTk+nTk;
            fourMom fourTk = pTk+nTk+pMu+nMu;
            // preselection
            if ( pMu.transverse() < 5.0 ) continue;
            if ( nMu.transverse() < 5.0 ) continue;
            if ( pMu.Momentum()   < 5.0 ) continue;
            if ( nMu.Momentum()   < 5.0 ) continue;
            if ( pTk.transverse() < 1.0 ) continue;
            if ( nTk.transverse() < 1.0 ) continue;
            if ( pTk.Momentum()   < 1.0 ) continue;
            if ( nTk.Momentum()   < 1.0 ) continue;

            if ( fourTk.transverse()< 12. ) continue;
            if ( fourTk.Momentum()  < 12. ) continue;


            const reco::Vertex* _vtx = usefulFuncs::get<reco::Vertex>( cand, "fitVertex" );
            if ( _vtx == nullptr ) continue;
            double fdSig = usefulFuncs::getFlightDistanceSignificance ( cand, &bs );
            if ( fdSig < 3.0 ) continue;
            double cos2d = usefulFuncs::getCosa2d( cand, &bs );
            double vtxprob = TMath::Prob( _vtx->chi2(), _vtx->ndof() );
            if ( cos2d < 0.99 ) continue;
            if ( vtxprob < 0.15 ) continue;

            candsSorted.emplace_back( vtxprob, &cand );
        }
        if ( candsSorted.size() == 0 ) return;
        // preselect for pCand end }}}
        // preselection for nCand {{{
        if ( !antiCandHandle.isValid() ) return;
        if ( antiCandHandle->size() == 0 ) return;

        std::vector< std::pair< double, const pat::CompositeCandidate*> > antiCandSort;
        antiCandSort.clear();
        antiCandSort.reserve( antiCandHandle->size() );
        handleIter = antiCandHandle->begin();
        handleIend = antiCandHandle->end  ();
        while( handleIter != handleIend )
        {
            const pat::CompositeCandidate& cand = *handleIter++;
            if ( !cand.hasUserFloat("fitMass") ) continue;
            if ( !cand.hasUserData("TkTk/Proton.fitMom") ) continue;
            if ( !cand.hasUserData(  "TkTk/Kaon.fitMom") ) continue;
            if ( !cand.hasUserFloat("TkTk/Proton.IPt") ) continue;
            if ( !cand.hasUserFloat(  "TkTk/Kaon.IPt") ) continue;
            if ( !cand.hasUserData( "fitVertex" ) ) continue;
            if ( !cand.hasUserData( "refToJPsi" ) ) continue;

            const GlobalVector* dPTR[2] = {nullptr};
            dPTR[0] = cand.userData<GlobalVector>("TkTk/Proton.fitMom");
            dPTR[1] = cand.userData<GlobalVector>("TkTk/Kaon.fitMom");

            const GlobalVector* muPTR[2] = {nullptr};
            muPTR[0] = cand.userData<GlobalVector>("JPsi/MuPos.fitMom");
            muPTR[1] = cand.userData<GlobalVector>("JPsi/MuNeg.fitMom");

            fourMom pMu ( muPTR[0]->x(), muPTR[0]->y(), muPTR[0]->z() );
            fourMom nMu ( muPTR[1]->x(), muPTR[1]->y(), muPTR[1]->z() );
            fourMom pTk ( dPTR[0]->x(), dPTR[0]->y(), dPTR[0]->z() );
            fourMom nTk ( dPTR[1]->x(), dPTR[1]->y(), dPTR[1]->z() );
            //fourMom tktk = pTk+nTk;
            fourMom fourTk = pTk+nTk+pMu+nMu;
            // preselection
            if ( pMu.transverse() < 5.0 ) continue;
            if ( nMu.transverse() < 5.0 ) continue;
            if ( pMu.Momentum()   < 5.0 ) continue;
            if ( nMu.Momentum()   < 5.0 ) continue;
            if ( pTk.transverse() < 1.0 ) continue;
            if ( nTk.transverse() < 1.0 ) continue;
            if ( pTk.Momentum()   < 1.0 ) continue;
            if ( nTk.Momentum()   < 1.0 ) continue;

            if ( fourTk.transverse()< 12. ) continue;
            if ( fourTk.Momentum()  < 12. ) continue;


            const reco::Vertex* _vtx = usefulFuncs::get<reco::Vertex>( cand, "fitVertex" );
            if ( _vtx == nullptr ) continue;
            double fdSig = usefulFuncs::getFlightDistanceSignificance ( cand, &bs );
            if ( fdSig < 3.0 ) continue;
            double cos2d = usefulFuncs::getCosa2d( cand, &bs );
            double vtxprob = TMath::Prob( _vtx->chi2(), _vtx->ndof() );
            if ( cos2d < 0.99 ) continue;
            if ( vtxprob < 0.15 ) continue;

            antiCandSort.emplace_back( vtxprob, &cand );
        }
        if ( antiCandSort.size() == 0 ) return;
        // preselect for nCand end }}}

        std::vector< std::pair< std::pair<double,const pat::CompositeCandidate*>, std::pair<double,const pat::CompositeCandidate*> > > pairCandidates;
        pairCandidates = pairpnCands( candsSorted, antiCandSort ); 
        std::cout << "cand size: " << _handle->size() <<  ", pn pair size: " << pairCandidates.size() << std::endl;
        

        std::vector< std::pair< std::pair<double,const pat::CompositeCandidate*>, std::pair<double,const pat::CompositeCandidate*> > >::const_iterator iter = pairCandidates.cbegin();
        std::vector< std::pair< std::pair<double,const pat::CompositeCandidate*>, std::pair<double,const pat::CompositeCandidate*> > >::const_iterator iend = pairCandidates.cend  ();

        while ( iter != iend )
        {
            Clear();
            const std::pair<double,const pat::CompositeCandidate*>& pSet = iter->first;
            const std::pair<double,const pat::CompositeCandidate*>& nSet = iter->second;
            ++iter;

            const pat::CompositeCandidate* pCand = pSet.second;
            const pat::CompositeCandidate* nCand = nSet.second;
 
            bool pForbid = true;
            bool nForbid = true;
            // pos particle rebuilt {{{
            // first one is proton and second one is kaon ( consider bigger momentum with heavier particle )
            const GlobalVector* pDaugsPTR[4] = {nullptr};
            pDaugsPTR[0] = pCand->userData<GlobalVector>("JPsi/MuPos.fitMom");
            pDaugsPTR[1] = pCand->userData<GlobalVector>("JPsi/MuNeg.fitMom");
            pDaugsPTR[2] = pCand->userData<GlobalVector>("TkTk/Proton.fitMom");
            pDaugsPTR[3] = pCand->userData<GlobalVector>("TkTk/Kaon.fitMom");

            fourMom pMuPos ( pDaugsPTR[0]->x(), pDaugsPTR[0]->y(), pDaugsPTR[0]->z() );
            fourMom pMuNeg ( pDaugsPTR[1]->x(), pDaugsPTR[1]->y(), pDaugsPTR[1]->z() );
            pMuPos.setMass( 0.1056583745 );
            pMuNeg.setMass( 0.1056583745 );
            fourMom pTkPos ( pDaugsPTR[2]->x(), pDaugsPTR[2]->y(), pDaugsPTR[2]->z() );
            fourMom pTkNeg ( pDaugsPTR[3]->x(), pDaugsPTR[3]->y(), pDaugsPTR[3]->z() );
            fourMom  pJPsi = pMuPos + pMuNeg;
            fourMom pTkTk;
            fourMom pFourTk;

            // find for PID.
            std::vector<fourMom> pDaug;
            pDaug.reserve( 3 );
            pDaug.emplace_back( pTkPos );
            pDaug.emplace_back( pTkNeg );
            pDaug.emplace_back(  pJPsi );
            MatchRes pMcRes = matchMC_CompositeCand( *pCand, pDaug, 1.0 );

            if ( pMcRes.isValid() )
            {
                // only choose lambda0_b
                pForbid = (pMcRes.getCand()->pdgId() !=  5122) ? true : false;
                for ( unsigned int i=0; i< pMcRes.getNDaughterRecorded(); ++i )
                {
                    unsigned pMcDaugID = pMcRes.getmcDaugID(i);
                    const reco::GenParticle* pMatchCand = pMcRes.getCand();
                    const reco::Candidate* pMcDaug = pMatchCand->daughter(pMcDaugID);
                    if ( pMcRes.getDaugID(i) == 0 ) // 0 == ptk
                    {
                        dataI[pptonPID]    = pMcDaug->pdgId();
                        dataI[pptonMomPID] = pMcDaug->mother()->pdgId();
                    }
                    if ( pMcRes.getDaugID(i) == 1 ) // 1 == ntk
                    {
                        dataI[pkaonPID]    = pMcDaug->pdgId();
                        dataI[pkaonMomPID] = pMcDaug->mother()->pdgId();
                    }
                } // find for pID end

                // search for pentaQuark
                // jpsip = jpsi + proton, jpsiP = jpsi + anti-proton
                fourMom pJpsip, pJpsipBar;
                pTkPos.setMass( protonMass );
                pTkNeg.setMass( protonMass );
                pJpsip = pMuPos + pMuNeg + pTkPos;
                pJpsipBar = pMuPos + pMuNeg + pTkNeg;

                dataD[ptargetJpsiP_mass] = pJpsip.Mag();
                dataD[ptargetJpsiP_pt] = pJpsip.transverse();
                dataD[ptargetJpsiPBar_mass] = pJpsipBar.Mag();
                dataD[ptargetJpsiPBar_pt] = pJpsipBar.transverse();

                // search for lam0
                pTkPos.setMass( protonMass );
                pTkNeg.setMass(   pionMass );
                pTkTk = pTkPos + pTkNeg;
                pFourTk = pMuPos + pMuNeg + pTkTk;

                dataD[pfake_Lam0Mass] = pTkTk.Mag();
                dataD[pfake_LbL0Mass] = pFourTk.Mag();

                // search for k short
                pTkPos.setMass( pionMass );
                pTkNeg.setMass( pionMass );
                pTkTk = pTkPos + pTkNeg;
                pFourTk = pMuPos + pMuNeg + pTkTk;

                dataD[pfake_KshortMass] = pTkTk.Mag();
                dataD[pfake_mumupipiMass] = pFourTk.Mag();

                // search for k(892)
                pTkPos.setMass( kaonMass );
                pTkNeg.setMass( pionMass );
                pTkTk = pTkPos + pTkNeg;
                pFourTk = pMuPos + pMuNeg + pTkTk;

                dataD[pfake_KstarMass] = pTkTk.Mag();
                dataD[pfake_BdMass] = pFourTk.Mag();

                // search for phi(1020)
                pTkPos.setMass( kaonMass );
                pTkNeg.setMass( kaonMass );
                pTkTk = pTkPos + pTkNeg;
                pFourTk = pMuPos + pMuNeg + pTkTk;

                dataD[pfake_PhiMass] = pTkTk.Mag();
                dataD[pfake_BsMass] = pFourTk.Mag();
            }
            // pos particle rebuilt end }}}
            // neg particle rebuilt {{{
            // first one is proton and second one is kaon ( consider bigger momentum with heavier particle )
            const GlobalVector* nDaugsPTR[4] = {nullptr};
            nDaugsPTR[0] = nCand->userData<GlobalVector>("JPsi/MuPos.fitMom");
            nDaugsPTR[1] = nCand->userData<GlobalVector>("JPsi/MuNeg.fitMom");
            nDaugsPTR[2] = nCand->userData<GlobalVector>("TkTk/Proton.fitMom");
            nDaugsPTR[3] = nCand->userData<GlobalVector>("TkTk/Kaon.fitMom");

            fourMom nMuPos ( nDaugsPTR[0]->x(), nDaugsPTR[0]->y(), nDaugsPTR[0]->z() );
            fourMom nMuNeg ( nDaugsPTR[1]->x(), nDaugsPTR[1]->y(), nDaugsPTR[1]->z() );
            nMuPos.setMass( 0.1056583745 );
            nMuNeg.setMass( 0.1056583745 );
            fourMom nTkPos ( nDaugsPTR[2]->x(), nDaugsPTR[2]->y(), nDaugsPTR[2]->z() );
            fourMom nTkNeg ( nDaugsPTR[3]->x(), nDaugsPTR[3]->y(), nDaugsPTR[3]->z() );
            fourMom nJPsi = nMuPos + nMuNeg;
            fourMom nTkTk;
            fourMom nFourTk;
            // find for PID.
            std::vector<fourMom> nDaug;
            nDaug.reserve( 3 );
            nDaug.emplace_back( nTkPos );
            nDaug.emplace_back( nTkNeg );
            nDaug.emplace_back(  nJPsi );
            MatchRes nMcRes = matchMC_CompositeCand( *nCand, nDaug, 1.0 );

            if ( nMcRes.isValid() )
            {
                // only choose lambda0_b
                nForbid = (nMcRes.getCand()->pdgId() != -5122) ? true : false;
                for ( unsigned int i=0; i< nMcRes.getNDaughterRecorded(); ++i )
                {
                    unsigned nMcDaugID = nMcRes.getmcDaugID(i);
                    const reco::GenParticle* nMatchCand = nMcRes.getCand();
                    const reco::Candidate* nMcDaug = nMatchCand->daughter(nMcDaugID);
                    if ( nMcRes.getDaugID(i) == 0 ) // 0 == ptk
                    {
                        dataI[nptonPID]    = nMcDaug->pdgId();
                        dataI[nptonMomPID] = nMcDaug->mother()->pdgId();
                    }
                    if ( nMcRes.getDaugID(i) == 1 ) // 1 == ntk
                    {
                        dataI[nkaonPID]    = nMcDaug->pdgId();
                        dataI[nkaonMomPID] = nMcDaug->mother()->pdgId();
                    }
                } // find for pID end

                // search for pentaQuark
                // jpsip = jpsi + proton, jpsiP = jpsi + anti-proton
                fourMom nJpsip, nJpsipBar;
                nTkPos.setMass( protonMass );
                nTkNeg.setMass( protonMass );
                nJpsip = nMuPos + nMuNeg + nTkPos;
                nJpsipBar = nMuPos + nMuNeg + nTkNeg;

                dataD[ntargetJpsiP_mass] = nJpsip.Mag();
                dataD[ntargetJpsiP_pt] = nJpsip.transverse();
                dataD[ntargetJpsiPBar_mass] = nJpsipBar.Mag();
                dataD[ntargetJpsiPBar_pt] = nJpsipBar.transverse();

                // search for lam0
                nTkPos.setMass( protonMass );
                nTkNeg.setMass(   pionMass );
                nTkTk = nTkPos + nTkNeg;
                nFourTk = nMuPos + nMuNeg + nTkTk;

                dataD[nfake_Lam0Mass] = nTkTk.Mag();
                dataD[nfake_LbL0Mass] = nFourTk.Mag();

                // search for k short
                nTkPos.setMass( pionMass );
                nTkNeg.setMass( pionMass );
                nTkTk = nTkPos + nTkNeg;
                nFourTk = nMuPos + nMuNeg + nTkTk;

                dataD[nfake_KshortMass] = nTkTk.Mag();
                dataD[nfake_mumupipiMass] = nFourTk.Mag();

                // search for k(892)
                nTkPos.setMass( kaonMass );
                nTkNeg.setMass( pionMass );
                nTkTk = nTkPos + nTkNeg;
                nFourTk = nMuPos + nMuNeg + nTkTk;

                dataD[nfake_KstarMass] = nTkTk.Mag();
                dataD[nfake_BdMass] = nFourTk.Mag();

                // search for phi(1020)
                nTkPos.setMass( kaonMass );
                nTkNeg.setMass( kaonMass );
                nTkTk = nTkPos + nTkNeg;
                nFourTk = nMuPos + nMuNeg + nTkTk;

                dataD[nfake_PhiMass] = nTkTk.Mag();
                dataD[nfake_BsMass] =  nFourTk.Mag();
            }
            // neg particle rebuilt end }}}
            // if p & n candidates are not lambda0_b, continue
            if ( pForbid && nForbid ) continue;


            //const pat::CompositeCandidate* pJpsi = usefulFuncs::getByRef<pat::CompositeCandidate>( *pCand, "refToJPsi" );
            //const reco::Vertex* pv = usefulFuncs::get<reco::Vertex>( *pJpsi, "fitVertex" );

            dataD[plbtkMass] = pCand->userFloat( "fitMass" );
            dataD[plbtkFlightDistance2d] = usefulFuncs::getFlightDistance ( *pCand, &bs );
            dataD[plbtkFlightDistanceSig]= usefulFuncs::getFlightDistanceSignificance ( *pCand, &bs );

            const reco::Vertex* pCandVtx = usefulFuncs::get<reco::Vertex>( *pCand, "fitVertex" );
            dataD[plbtkVtxprob] = TMath::Prob( pCandVtx->chi2(), pCandVtx->ndof() );
            dataD[plbtkCosa2d] = usefulFuncs::getCosa2d(*pCand,&bs);

            dataD[plbtkMom]= pFourTk.Momentum();
            dataD[plbtkPt] = pFourTk.transverse();
            dataD[ptktkPt] = pTkTk.transverse();
            dataD[ptktkMom]= pTkTk.Momentum();
            dataD[pptonPt]  = pTkPos.transverse();
            dataD[pkaonPt]  = pTkNeg.transverse();
            dataD[pptonMom] = pTkPos.Momentum();
            dataD[pkaonMom] = pTkNeg.Momentum();
            dataD[pptonIPt] = pCand->userFloat("TkTk/Proton.IPt");
            dataD[pkaonIPt] = pCand->userFloat("TkTk/Kaon.IPt");
            dataD[pptonIPtErr] = pCand->userFloat("TkTk/Proton.IPt.Error");
            dataD[pkaonIPtErr] = pCand->userFloat("TkTk/Kaon.IPt.Error");
            if ( pCand->hasUserFloat("TkTk/Proton.dEdx.pixelHrm") )
                dataD[pptonDEDX_pixelHrm] = pCand->userFloat( "TkTk/Proton.dEdx.pixelHrm" );
            if ( pCand->hasUserFloat(  "TkTk/Kaon.dEdx.pixelHrm") )
                dataD[pkaonDEDX_pixelHrm] = pCand->userFloat( "TkTk/Kaon.dEdx.pixelHrm" );
            if ( pCand->hasUserFloat("TkTk/Proton.dEdx.Harmonic") )
                dataD[pptonDEDX_Harmonic] = pCand->userFloat( "TkTk/Proton.dEdx.Harmonic" );
            if ( pCand->hasUserFloat(  "TkTk/Kaon.dEdx.Harmonic") )
                dataD[pkaonDEDX_Harmonic] = pCand->userFloat(   "TkTk/Kaon.dEdx.Harmonic" );




            //const pat::CompositeCandidate* nJpsi = usefulFuncs::getByRef<pat::CompositeCandidate>( *nCand, "refToJPsi" );
            //const reco::Vertex* pv = usefulFuncs::get<reco::Vertex>( *nJpsi, "fitVertex" );

            dataD[nlbtkMass] = nCand->userFloat( "fitMass" );
            dataD[nlbtkFlightDistance2d] = usefulFuncs::getFlightDistance ( *nCand, &bs );
            dataD[nlbtkFlightDistanceSig]= usefulFuncs::getFlightDistanceSignificance ( *nCand, &bs );

            const reco::Vertex* nCandVtx = usefulFuncs::get<reco::Vertex>( *nCand, "fitVertex" );
            dataD[nlbtkVtxprob] = TMath::Prob( nCandVtx->chi2(), nCandVtx->ndof() );
            dataD[nlbtkCosa2d] = usefulFuncs::getCosa2d(*nCand,&bs);

            dataD[nlbtkMom]= nFourTk.Momentum();
            dataD[nlbtkPt] = nFourTk.transverse();
            dataD[ntktkPt] = nTkTk.transverse();
            dataD[ntktkMom]= nTkTk.Momentum();
            dataD[nptonPt]  = nTkPos.transverse();
            dataD[nkaonPt]  = nTkNeg.transverse();
            dataD[nptonMom] = nTkPos.Momentum();
            dataD[nkaonMom] = nTkNeg.Momentum();
            dataD[nptonIPt] = nCand->userFloat("TkTk/Proton.IPt");
            dataD[nkaonIPt] = nCand->userFloat("TkTk/Kaon.IPt");
            dataD[nptonIPtErr] = nCand->userFloat("TkTk/Proton.IPt.Error");
            dataD[nkaonIPtErr] = nCand->userFloat("TkTk/Kaon.IPt.Error");
            if ( nCand->hasUserFloat("TkTk/Proton.dEdx.pixelHrm") )
                dataD[nptonDEDX_pixelHrm] = nCand->userFloat( "TkTk/Proton.dEdx.pixelHrm" );
            if ( nCand->hasUserFloat(  "TkTk/Kaon.dEdx.pixelHrm") )
                dataD[nkaonDEDX_pixelHrm] = nCand->userFloat( "TkTk/Kaon.dEdx.pixelHrm" );
            if ( nCand->hasUserFloat("TkTk/Proton.dEdx.Harmonic") )
                dataD[nptonDEDX_Harmonic] = nCand->userFloat( "TkTk/Proton.dEdx.Harmonic" );
            if ( nCand->hasUserFloat(  "TkTk/Kaon.dEdx.Harmonic") )
                dataD[nkaonDEDX_Harmonic] = nCand->userFloat(   "TkTk/Kaon.dEdx.Harmonic" );
            thisTree()->Fill();

        }

    } catch (...) {}
}

void treeMainGen_pnLbTk::RegTree()
{
    TTree* t = thisTree();
    RegFormatTree(t);

    t->Branch( "pptonPID", &dataI[pptonPID], "pptonPID/I" );
    t->Branch( "pkaonPID", &dataI[pkaonPID], "pkaonPID/I" );
    t->Branch( "pptonMomPID", &dataI[pptonMomPID], "pptonMomPID/I" );
    t->Branch( "pkaonMomPID", &dataI[pkaonMomPID], "pkaonMomPID/I" );
    t->Branch( "nptonPID", &dataI[nptonPID], "nptonPID/I" );
    t->Branch( "nkaonPID", &dataI[nkaonPID], "nkaonPID/I" );
    t->Branch( "nptonMomPID", &dataI[nptonMomPID], "nptonMomPID/I" );
    t->Branch( "nkaonMomPID", &dataI[nkaonMomPID], "nkaonMomPID/I" );
    return;
}
void treeMainGen_pnLbTk::GetByLabel( fwlite::Event* ev )
{
    getByLabel_Cand( ev );
    getByLabel_antiCand( ev );
    getByLabel_genParticle( ev );
    getByLabel_BS( ev );
    getByLabel_PV( ev );
}

inline void treeMainGen_pnLbTk::getByLabel_BS( fwlite::Event* ev )
{ beamSpotHandle.getByLabel( *ev,"offlineBeamSpot", "", "RECO"  ); return; }
inline void treeMainGen_pnLbTk::getByLabel_PV( fwlite::Event* ev )
{ primaryVHandle.getByLabel( *ev,"offlinePrimaryVertices", "", "RECO"  ); return; }
inline void treeMainGen_pnLbTk::getByLabel_antiCand( fwlite::Event* ev )
{ antiCandHandle.getByLabel( *ev, antiCandLabel.module.c_str(), antiCandLabel.label.c_str(), antiCandLabel.process.c_str() ); return; }
inline std::vector< std::pair< std::pair<double,const pat::CompositeCandidate*>, std::pair<double,const pat::CompositeCandidate*> > > treeMainGen_pnLbTk::pairpnCands
( std::vector<std::pair<double,const pat::CompositeCandidate*> >& pCands, std::vector<std::pair<double, const pat::CompositeCandidate*> >& nCands )
{
    unsigned NpCands = pCands.size();
    unsigned NnCands = nCands.size();

    std::vector< std::pair< std::pair<double,const pat::CompositeCandidate*>, std::pair<double,const pat::CompositeCandidate*> > > pairpnCandList;
    pairpnCandList.reserve( NpCands );
    std::vector< unsigned > idxPairHistory;
    idxPairHistory.reserve( NpCands );
    for ( unsigned i = 0; i < NpCands; ++i )
    {
        const pat::CompositeCandidate* pcompcand = pCands[i].second;

        //double logDeltaR = 999.;
        unsigned reserveJ = 999;
        

        for ( unsigned j = 0; j < NnCands; ++j )
        {
            const pat::CompositeCandidate* ncompcand = nCands[j].second;
            if ( theSameCompCand(pcompcand, ncompcand) )
                reserveJ = j;
        }
        if ( reserveJ == 999 ) continue;

        // check whether it is repeated to find the same index
        for ( const auto idx : idxPairHistory )
            if ( reserveJ == idx )
                printf( "\nWarning!!! in pairpnCands function: there are j idx repeating paired: (i,j) = (%d,%d)\n", i,reserveJ );

        pairpnCandList.push_back( std::make_pair(pCands[i], nCands[reserveJ]) );
        idxPairHistory.push_back( reserveJ );
    }
    return pairpnCandList;
}
void treeMainGen_pnLbTk::setBranchAddress( TTree* inputTree )
{
    LoadFormatSourceBranch(inputTree);

    inputTree->SetBranchAddress( "pptonPID", &dataI[pptonPID] );
    inputTree->SetBranchAddress( "pkaonPID", &dataI[pkaonPID] );
    inputTree->SetBranchAddress( "pptonMomPID", &dataI[pptonMomPID] );
    inputTree->SetBranchAddress( "pkaonMomPID", &dataI[pkaonMomPID] );
    inputTree->SetBranchAddress( "nptonPID", &dataI[nptonPID] );
    inputTree->SetBranchAddress( "nkaonPID", &dataI[nkaonPID] );
    inputTree->SetBranchAddress( "nptonMomPID", &dataI[nptonMomPID] );
    inputTree->SetBranchAddress( "nkaonMomPID", &dataI[nkaonMomPID] );
    return;
}
bool treeMainGen_pnLbTk::theSameCompCand( const pat::CompositeCandidate* cand1, const pat::CompositeCandidate* cand2 )
{
    if ( cand1->numberOfDaughters() != cand2->numberOfDaughters() ) return false;
    const reco::Candidate* dau10 = cand1->daughter(0);
    const reco::Candidate* dau11 = cand1->daughter(1);
    const reco::Candidate* dau12 = cand1->daughter(2);
    const reco::Candidate* dau13 = cand1->daughter(3);
    const reco::Candidate* dau20 = cand2->daughter(0);
    const reco::Candidate* dau21 = cand2->daughter(1);
    const reco::Candidate* dau22 = cand2->daughter(2);
    const reco::Candidate* dau23 = cand2->daughter(3);
    bool dR00 = theSameDaugs( dau10, dau20, 0.00001 );
    bool dR01 = theSameDaugs( dau10, dau21, 0.00001 );
    bool dR10 = theSameDaugs( dau11, dau20, 0.00001 );
    bool dR11 = theSameDaugs( dau11, dau21, 0.00001 );
    bool dR22 = theSameDaugs( dau12, dau22, 0.00001 );
    bool dR23 = theSameDaugs( dau12, dau23, 0.00001 );
    bool dR32 = theSameDaugs( dau13, dau22, 0.00001 );
    bool dR33 = theSameDaugs( dau13, dau23, 0.00001 );

    short result = 2;
    if ( (dR00 && dR11) || (dR10&&dR01) ) --result;
    if ( (dR22 && dR33) || (dR23&&dR32) ) --result;
    return result == 0 ? true : false;
}
