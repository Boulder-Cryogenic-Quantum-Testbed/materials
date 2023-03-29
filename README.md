# materials
A comprehensive list of materials losses at millikelvin temperatures and single photon powers

<iframe width="900" height="800" frameborder="0" scrolling="no" src="//plotly.com/~crmcrae/1.embed"></iframe>

<details><summary>DIELECTRIC MATERIALS</summary>
<p>

Dielectric material measurements. Columns (from left to right): material of interest (Material), reference where the measurement is reported (Reference), method of dielectric deposition (Dep.), design of the measured device (Geom.), reported low power loss δ_LP, and resonator-induced intrinsic TLS loss Fδ^0_TLS. CVD: chemical vapor deposition. Therm. ox.: thermal oxidation. PECVD: plasma-enhanced CVD. ICP CVD: inductively coupled plasma CVD. MBE: molecular beam epitaxy. ECR-PECVD: electron cyclotron resonance PECVD. LE: lumped element resonator design. LE PPC: lumped element resonator with the parallel plate capacitor. IDC: lumped element resonator with the interdigitated capacitor.

Note that values cannot be directly compared due to differences in the TLS filling factor, resonance frequency, Qi/Qc matching, fabrication, magnetic shielding, IR filtering and isolation, thermalization, and data fitting.

|  Material  | Reference | Dep. | Geom. | δ_LP [x 10^-5] | Fδ^0_TLS [x 10^-5] |
| ---------- | --------- | ---- | ----- | ----------- | --------------- |
| LaAlO3 | Degnan 2022[^Degnan2022] | Substrate | CPW |  | 0.91 |
| MgAl2O4 | Degnan 2022[^Degnan2022] | Substrate | CPW | | 0.5 |
| a-SiC:H | Buijtendorp 2021[^Buijtendorp2021] | PECVD | Microstrip |  | 3.2 |
| a-Si | Hahnle 2021[^Hahnle2021] | PECVD | Microstrip |  | 3.7 |
| a-Ge | Kopas 2021[^Kopas2021] | Therm. evap. | CPW| 0.47-1.1 | |
| InGaAs/InAs/InGaAs/InAlAs stack on InP | Phan 2021^[Phan2021] | MBE | CPW | 40 |  |
| Al2O3 | McRae 2020[^McRae2020] | Sputter | LE PPC | | 100 |
| HSQ | Niepce 2020[^Niepce2020] | Spin-on-glass | CPW |  800 | |
| B4C | Wisbey 2019[^Wisbey2019] | Sputter | CPW | | 10-15 |
| BN | Wisbey 2019[^Wisbey2019] | Sputter | CPW | | 6 |
| AlOx | Brehm 2017[^Brehm2017] | Anodic ox. | CPW + PPC | | 4-22 |
| a-Si | Lecocq 2017[^Lecocq2017] | PECVD | LE PPC | 15-50 | |
| SiN | Duff 2016[^Duff2016] | ICP-PECVD | Microstrip |  | 78 |
| SiO2 | Goetz 2016[^Goetz2016] | Therm. ox. | CPW |  | 0.34-0.89 |
| SiNx | Sarabi 2016[^Sarabi2016] | PECVD | LE PPC | 78 | |
| AlOx | Deng 2014[^Deng2014] | Plasma ox. | LE overlap | 140-180 | |
| HfO2 | Burnett 2013[^Burnett2013] | Sputter | LE IDC | | 1.5-2.5 |
| Al2O3 | Burnett 2013[^Burnett2013] | Sputter | LE IDC | | 2.0-2.5 |
| Al2O3 | Cho 2013[^Cho2013] | PLD | LE PPC | 3-5 | |
| SiOx | Li 2013[^Li2013] | ECR-PECVD | Microstrip | 100-700 | |
| AlOx | Pappas 2011[^Pappas2011] | Therm. ox. | CPW | | F x 100 |
| Al2O3 | Weides 2011[^Weides2011] | MBE | LE PPC | 6 | |
| a-SiO2 | Cicak 2010[^Cicak2010] | ECR-PECVD | LE PPC | 600 | |
| a-SiN | Cicak 2010[^Cicak2010] | ECR-PECVD | LE PPC | 40-50 | |
| a-Si | Cicak 2010[^Cicak2010] | Sputter | LE PPC | 150-200 | |
| Nb2O5 | Kaiser 2010[^Kaiser2010] | Anodic ox. | LE PPC | 100-400 | |
| SiO | Kaiser 2010[^Kaiser2010] | Therm. evap. | LE PPC | 20-50 | |
| SiNx | Kaiser 2010[^Kaiser2010] | PECVD | LE PPC | 10-30 | |
| a-SiN | Paik 2010[^Paik2010] | ICP CVD | LE PPC | 2.5-120 | |
| a-Si:H | OConnell 2008[^OConnell2008] | NA | LE PPC, CPW | 1-13 | |
| SiNx | OConnell 2008[^OConnell2008] | NA | LE PPC, CPW | 10-20 | |
| SiO2 | OConnell 2008[^OConnell2008] | Therm. ox. | CPW | 30-33 | |
| Si | OConnell 2008[^OConnell2008] | Sputtered | CPW | 50-60 | |
| AlN | OConnell 2008[^OConnell2008] | NA | CPW | 110-180 | |
| SiO2 | OConnell 2008[^OConnell2008] | PECVD | CPW | 270-290 | |
| MgO | OConnell 2008[^OConnell2008] | NA | CPW | 500-800 | |
| a-SiO2 | Martinis 2005[^Martinis2005] | CVD  | LE PPC | 500 | |
| a-SiNx | Martinis 2005[^Martinis2005] | CVD | LE PPC | 20 | |


</p>
</details>

<details><summary>THIN FILM SUPERCONDUCTING METALS</summary>
<p>

Loss measurements of superconducting metals. Columns (from left to right): superconductor in the measured device (SC), reference where the measurement is reported (Reference), method of metal deposition (Dep.), surface treatments applied and etch type used to define resonators (Surf./Etch), substrate on which the metal was deposited (Substrate), design of the measured device (Geom.), reported low power loss δLP, resonator-induced intrinsic TLS loss Fδ^0_TLS, width w of the conductor, and gap g between the conductor and the ground plane. Therm. evap.:
thermal evaporation. MBE: molecular beam epitaxy. PVD: plasma vapor deposition. RIE: reactive ion etch. H-pass.: hydrogen-passivated. λ/2 or λ/4: CPW resonator of length stated. LE IDC: lumped element resonator with the interdigitated capacitor. NA: information not available.

Note that values cannot be directly compared due to significant experimental differences.

|  SC  | Reference | Dep. | Surf./Etch | Substrate | Geom. | δ_LP [x 10^-6] | Fδ^0_TLS [x 10^-6] | w/g |
| ---- | --------- | ---- | ---------- | --------- | ----- | ------------------- | ----------------------- | --- |
| NbN/TiN  | Kim2021[^Kim2021] | Sputter | NA / RIE | Si | λ/2 | 3.68 |  |  |
| Nb  | Zheng2022[^Zheng2022] | E-beam | BOE / RIE | Si | λ/4 |  | 0.29 | 3/2 |
| Nb  | Kowsari2021[^Kowsari2021] | E-beam  | Piranha+BOE / RIE | Si | λ/4 |  | 0.194 | 3/2 |
| TiN  | Gao2021[^Gao2021] | MBE  | 300C anneal / RIE | Al2O3 | λ/2 hanger | 0.3 |  | 10/6 |
| TiN  | Gao2021[^Gao2021] | MBE  | 300C anneal / wet etch | Al2O3 | λ/2 hanger | 0.3 |  | 10/6 |
| TiN  | Lock2019[^Lock2019] | Sputter | HF / RIE |  Si  |  λ/4  | | 0.2-30 | 3/12 |
| Nb  | Nersisyan2019[^Nersisyan2019] | PVD | Various / RIE |  Si  |  λ/4  | 0.8-6 | |
| TiN  | Woods2019[^Woods2019] | Sputter | RCA / RIE |  Si  |  λ/4  | | 0.3-1 |
| Al  | Burnett 2018[^Burnett2018] | E-beam | HF / wet etch |  Si  |  λ/4  | 1.3 | 1.1 |
| TiN  | Calusine 2018[^Calusine2018] | Sputter | RCA / RIE |  Si  |  λ/4   | | 0.3 | 16/8-22/11 |
| Al  | Earnest 2018[^Earnest2018] | E-beam | none / RIE |  Si  |  λ/4  | 3.1 | 3.27 | 15/9 |
| Al  | Earnest 2018[^Earnest2018] | E-beam | RCA-1+HF / RIE |  Si  |  λ/4  | 1.9 | 1.53 | 15/9 |
| Al  | Earnest 2018[^Earnest2018] | E-beam | Anneal / RIE |  Si  |  λ/4  | 1.8 | 1.56 | 15/9 |
| Al  | Earnest 2018[^Earnest2018] | E-beam | RCA-1+HF+anneal / RIE |  Si  |  λ/4   | 1.2 | 0.8 | 15/9 |
| In  | McRae 2018[^McRae2018] | Therm. evap. | none / wet etch |  Si  |  λ/4  | | 40 | 12/6 |
| In  | McRae 2018[^McRae2018] | Therm. evap. | HF / wet etch |  Si  |  λ/4  | | 50 | 12/6 |
| TiN  | Shearrow 2018[^Shearrow2018] | ALD | Nano-Strip, HF / RIE |  Si  | LE IDC | 0.5-17 | |
| NbN  | DeGraaf 2017[^DeGraaf2017] | Sputter | none / NA |  Al2O3  | Fractal | | 10.4-10.6 | g=2|
| NbN  | DeGraaf 2017[^DeGraaf2017] | Sputter | Anneal / NA |  Al2O3  | Fractal | | 7.44, 7.69 | g=2|
| Nb+Pt  | Burnett 2016[^Burnett2016] | MBE | NA / RIE |  Al2O3  | LE IDC | | 12 | |
| Nb  | Burnett 2016[^Burnett2016] | Sputter | NA / RIE |  Al2O3  | Fractal | | 1.1 | |
| Nb  | Goetz 2016[^Goetz2016] | Sputter | HF / RIE |  Si  |  λ/2  | | 0.9 | 20/12 |
| Nb  | Goetz 2016[^Goetz2016] | Sputter | Ar mill / RIE |  Al2O3  |  λ/2  | | 1.6 | 20/12|
| Al  | Richardson 2016[^Richardson2016] | MBE | Various / wet etch |  Si  |  λ/4  | | 0.2-760 | 3/2-22/12|
| Al  | Richardson 2016[^Richardson2016] | MBE | Various / RIE |  Si  |  λ/4  | | 0.5-4800 | 3/2-22/12 |
| Al  | Richardson 2016[^Richardson2016] | MBE | Various / wet etch |  Al2O3  |  λ/4  | | 0.5-5.3 | 3/2-22/12|
| Al  | Richardson 2016[^Richardson2016] | MBE | Various / RIE |  Al2O3  |  λ/4  | | 0.4-7.4 | 3/2-22/12|
| TiN  | Ohya 2014[^Ohya2014] | Sputter | Nano-Strip+HF / RIE |  Si  |  λ/4  | 1 | | 15/10|
| Nb  | Burnett 2013[^Burnett2013] | Sputter | NA |  Al2O3  | LE IDC | | 2.0 | |
| Re  | Cho 2013[^Cho2013] | MBE | Anneal / NA |  Al2O3  | LE IDC | 30-50 | | |
| NbTiN  | Barends 2010b[^Barends2010b] | Sputter | H-pass., RIE |  Si  |  λ/4  | 3 | | 3/2-6/2 | 
| Ta  | Barends 2010b[^Barends2010b] | Sputter | NA, RIE |  Si  |  λ/4  | 30 | | 5/2 |
| Nb  | Macha 2010[^Macha2010] | NA | none / dry etch |  Al2O3  |  λ/2  | | 2.4-2.6 | 50/30 |
| Nb  | Macha 2010[^Macha2010] | NA | none / dry etch |  Si  |  λ/2  | | 1.3, 1.6 | 50/30 | 
| Al  | Macha 2010[^Macha2010] | NA | none / liftoff |  Al2O3  |  λ/2  | | 2.0 | 50/30 |
|  Re  | Wang 2009[^Wang2009] | E-beam | NA / RIE |  Al2O3  |  λ/4  | 1-3 | | 16/6.4-5/2 |
| Al  | Wang 2009[^Wang2009] | Sputter | NA / RIE |  Al2O3  |  λ/4  | 3-10 | | 16/6.4-5/2 |
| Nb | Gao 2008b[^Gao2008b] | NA | NA |  Al2O3  | λ/4  | | 2.4-29.8 | 3/2-50/33 |
| Nb | Kumar 2008[^Kumar2008] | NA | NA, RIE |  Si  |  λ/4  | | 29.4 | 5/1 | %| 5/1 |
| Al | O'Connell 2008[^OConnell2008] | NA | NA | Si |  λ/2  | <5-12 |
| Re | O'Connell 2008[^OConnell2008] | NA | NA |  Al2O3  |  λ/2  | <6-10 |
| Al | O'Connell 2008[^OConnell2008] | NA | NA |  Al2O3  |  λ/2  | <9-21 |
| Al | O'Connell 2008[^OConnell2008] | NA | NA |  Al2O3  | LE IDC | 41-47 |

</p>
</details>

REFERENCES

[^Martinis2005]: Martinis, J. M., Cooper, K. B., McDermott, R., Steffen, M., Ansmann, M., Osborn, K., Cicak, K., Oh, S., Pappas, D. P., Simmonds, R. W. et al., “Decoherence in Josephson qubits from dielectric loss,” Phys. Rev. Lett. 95, 210503 (2005)
[^OConnell2008]: O’Connell, A. D., Ansmann, M., Bialczak, R. C., Hofheinz, M., Katz, N.,Lucero,  E.,  McKenney,  C.,  Neeley,  M.,  Wang,  H.,  Weig,  E. M.,et al.,“Microwave dielectric loss at single photon energies and millikelvin temperatures,” Appl. Phys. Lett. 92, 112903 (2008)
[^Cicak2010]: Cicak, K., Li, D., Strong, J. A., Allman, M. S., Altomare, F., Sirois, A. J.,Whittaker, J. D., Teufel, J. D.,   and Simmonds, R. W., “Low-loss superconducting resonant circuits using vacuum-gap-based microwave components,” Appl. Phys. Lett. 96, 093502 (2010)
[^Kaiser2010]: Kaiser, C., Skacel, S., Wünsch, S., Dolata, R., Mackrodt, B., Zorin, A.,  andSiegel, M., “Measurement of dielectric losses in amorphous thin films at gigahertz frequencies using superconducting resonators,” Supercond. Sci.Technol.23, 075008 (2010)
[^Paik2010]: Paik, H. and Osborn, K. D., “Reducing quantum-regime dielectric loss of silicon nitride for superconducting quantum circuits,” Appl.  Phys. Lett. 96, 072505 (2010)
[^Pappas2011]: Pappas, D. P., Vissers, M. R., Wisbey, D. S., Kline, J. S., and Gao, J., “Two level system loss in superconducting microwave resonators,” IEEE Trans. Appl. Supercond. 21, 871–874 (2011)
[^Weides2011]: Weides, M. P., Kline, J. S., Vissers, M. R., Sandberg, M. O., Wisbey, D. S.,Johnson, B. R., Ohki, T. A.,  and Pappas, D. P., “Coherence in a transmonqubit with epitaxial tunnel junctions,” Appl. Phys. Lett. 99, 262502 (2011)
[^Burnett2013]: Burnett, J., Lindström, T., Oxborrow, M., Harada, Y., Sekine, Y., Meeson,P., and Tzalenchuk, A.Y., “Slow noise processes in superconducting resonators,” Phys. Rev. B 87, 140501 (2013)
[^Cho2013]: Cho, K.-H., Patel, U., Podkaminer, J., Gao, Y., Folkman, C., Bark, C., Lee, S.,Zhang, Y., Pan, X., McDermott, R.,et al., “Epitaxial Al2O3 capacitors forlow microwave loss superconducting quantum circuits,” APL Materials 1, 042115 (2013).
[^Li2013]: Li, D., Gao, J., Austermann, J., Beall, J., Becker, D., Cho, H.-M., Fox, A. E. Halverson, N., Henning, J., Hilton, G.,et al., “Improvements in silicon oxide dielectric loss for superconducting microwave detector circuits,” IEEE Trans. Appl. Supercond. 23, 1501204–1501204 (2013).
[^Deng2014]: Deng, C., Otto, M., and Lupascu, A., “Characterization of low-temperature microwave loss of thin aluminum oxide formed by plasma  oxidation,” Appl. Phys. Lett. 104, 043506 (2014)
[^Duff2016]: Duff, S. M., Austermann, J., Beall, J., Becker, D., Datta, R., Gallardo, P.,Henderson, S., Hilton, G., Ho, S., Hubmayr, J., et al., “Advanced actpol multichroic polarimeter array fabrication process for 150 mm wafers,” J.Low Temp. Phys. 184, 634–641 (2016)
[^Goetz2016]: Goetz, J., Deppe, F., Haeberlein, M., Wulschner, F., Zollitsch, C. W., Meier,S., Fischer, M., Eder, P., Xie, E., Fedorov, K. G., et al., “Loss mechanisms in superconducting thin film microwave resonators,” J. Appl. Phys. 119, 015304 (2016)
[^Lecocq2017]: Lecocq, F., Ranzani, L., Peterson, G., Cicak, K., Simmonds, R., Teufel, J., and Aumentado, J., “Nonreciprocal microwave signal processing with a field-programmable josephson amplifier,” Phys. Rev. Applied 7, 024028 (2017)
[^Sarabi2016]: Sarabi, B., Ramanayaka, A. N., Burin, A. L., Wellstood, F.C., and Osborn, K.D., “Projected dipole moments of individual two-level  defects extracted using circuit quantum electrodynamics,” Phys. Rev. Lett. 116,167002 (2016)
[^Brehm2017]: Brehm, J. D., Bilmes, A., Weiss, G., Ustinov, A. V., and Lisenfeld, J.,“Transmission-line resonators for the study of individual two-level tunneling systems,” Appl. Phys. Lett. 111, 112601 (2017)
[^Wisbey2019]: Wisbey, D. S., Vissers, M. R., Gao, J., Kline, J. S., Sandberg, M. O., Weides, M. P., Paquette, M., Karki, S., Brewster, J., Alameri, D., et al., “Dielectric loss of boron-based dielectrics on niobium resonators,” J. Low Temp. Phys. 195, 474–486 (2019)
[^McRae2020]: McRae, C. R. H., Lake, R. E., Long, J. L., Bal, M., Wu, X., Jugdersuren, B., Metcalf, T. H., Liu, X., and Pappas, D. P., “Dielectric loss extraction for superconducting microwave resonators,” Appl. Phys. Lett. 116, 194003 (2020)
[^Niepce2020]: Niepce, D., Burnett, J. J., Latorre, M. G.,  and Bylander, J., “Geometric scaling of two-level-system loss in superconducting resonators,” Supercond. Sci. Technol. 33, 025013 (2020)
[^Gao2008b]: Gao, J., Daal, M., Martinis, J. M., Vayonakis, A., Zmuidzinas, J., Sadoulet, B., Mazin, B. A., Day, P. K., and Leduc, H. G., “A semiempirical model for two-level system noise in superconducting microresonators,” Appl. Phys. Lett. 92, 212504 (2008b)
[^Kumar2008]: Kumar, S., Gao, J., Zmuidzinas, J., Mazin, B.A., LeDuc, H.G., and Day, P.K., “Temperature dependence of the frequency and noise of superconducting coplanar waveguide resonators,” Appl. Phys. Lett. 92, 123503 (2008)
[^OConnell2008]: O’Connell, A. D., Ansmann, M., Bialczak, R. C., Hofheinz, M., Katz, N., Lucero, E., McKenney, C., Neeley, M., Wang, H., Weig, E. M., et al., “Microwave dielectric loss at single photon energies and millikelvin temperatures,” Appl. Phys. Lett. 92, 112903 (2008)
[^Wang2009]: Wang, H., Hofheinz, M., Wenner, J., Ansmann, M., Bialczak, R., Lenander, M., Lucero, E., Neeley, M., O’Connell, A., Sank, D., et al., “Improving the coherence time of superconducting coplanar resonators,” Appl. Phys. Lett. 95, 233508 (2009)
[^Barends2010b]: Barends, R., Vercruyssen, N., Endo, A., De Visser, P., Zijlstra, T., Klapwijk, T., Diener, P., Yates, S., and Baselmans, J., “Minimal resonator loss for circuit quantum electrodynamics,” Appl. Phys. Lett. 97, 023508 (2010)
[^Macha2010]: Macha, P., van Der Ploeg, S., Oelsner, G., Ilichev, E., Meyer, H.-G., Wünsch, S., and Siegel, M., “Losses in coplanar waveguide resonators at millikelvin temperatures,” Appl. Phys. Lett. 96, 062503 (2010)
[^Burnett2013]: Burnett, J., Lindström, T., Oxborrow, M., Harada, Y., Sekine, Y., Meeson, P., and Tzalenchuk, A.Y., “Slow noise processes in superconducting resonators,” Phys. Rev. B 87, 140501 (2013)
[^Cho2013]: Cho, K.-H., Patel, U., Podkaminer, J., Gao, Y., Folkman, C., Bark, C., Lee, S., Zhang, Y., Pan, X., McDermott, R., et al., “Epitaxial Al2O3 capacitors for low microwave loss superconducting quantum circuits,” APL Materials 1, 042115 (2013)
[^Ohya2014]: Ohya, S., Chiaro, B., Megrant, A., Neill, C., Barends, R., Chen, Y., Kelly,J., Low, D., Mutus, J., O’Malley, P., et al., “Room temperature deposition of sputtered tin films for superconducting coplanar waveguide resonators, ”Supercond. Sci. Technol. 27, 015009 (2013)
[^Burnett2016]: Burnett, J., Faoro, L., and Lindström, T., “Analysis of high quality superconducting resonators: consequences for TLS properties in amorphous oxides, ”Supercond. Sci. Technol. 29, 044008 (2016)
[^Goetz2016]: Goetz, J., Deppe, F., Haeberlein, M., Wulschner, F., Zollitsch, C. W., Meier, S., Fischer, M., Eder, P., Xie, E., Fedorov, K. G., et al., “Loss mechanisms in superconducting thin film microwave resonators,” J. Appl. Phys. 119, 015304 (2016)
[^Richardson2016]: Richardson, C., Siwak, N., Hackley, J., Keane, Z., Robinson, J., Arey, B., Arslan, I., and Palmer, B., “Fabrication artifacts and parallel loss channels in metamorphic epitaxial aluminum superconducting resonators,” Supercond. Sci. Technol. 29, 064003 (2016)
[^DeGraaf2017]: De Graaf, S., Faoro, L., Burnett, J., Adamyan, A., Tzalenchuk, A. Y., Kubatkin, S., Lindström, T., and Danilov, A., “Suppression of low-frequency charge noise in superconducting resonators by surface spin desorption,” Nat. Commun. 9, 1143 (2018).
[^Shearrow2018]: Shearrow, A., Koolstra, G., Whiteley, S. J., Earnest, N., Barry, P. S., Heremans, F. J., Awschalom, D. D., Shirokoff, E., and Schuster, D. I., “Atomic layer deposition of titanium nitride for quantum circuits,” Appl. Phys. Lett. 113 (21), 212601 (2018).
[^McRae2018]: McRae, C. R. H., Béjanin, J. H., Earnest, C. T., McConkey, T. G., Rinehart, J. R., Deimert, C., Thomas, J. P., Wasilewski, Z. R., and Mariantoni, M., “Thin film metrology and microwave loss characterization ofindium and aluminum/indium superconducting planar resonators,” J. Appl. Phys. 123 (20), 205304 (2018).
[^Earnest2018]: Earnest, C. T., Béjanin, J. H., McConkey, T. G., Peters, E. A., Korinek, A., Yuan, H., and Mariantoni, M., “Substrate surface engineering for high-quality silicon/aluminium superconducting resonators,” Supercond. Sci. Technol. 31, 125013 (2018)
[^Calusine2018]: Calusine, G., Melville, A., Woods, W., Das, R., Stull, C., Bolkhovsky, V., Braje, D., Hover, D., Kim, D. K., Miloshi, X. et al., “Analysis and mitigation of interface losses in trenched superconducting coplanar waveguide resonators,” Appl. Phys. Lett. 112, 062601 (2018).
[^Burnett2018]: Burnett, J., Bengtsson, A., Niepce, D., and Bylander, J., “Noise and loss of superconducting aluminium resonators at single photon energies,” J. Phys. Conf. Ser. 969, 012131 (2018).
[^Woods2019]: Woods, W., Calusine, G., Melville, A., Sevi, A., Golden, E., Kim, D. K., Rosenberg, D., Yoder, J. L., and Oliver, W. D., “Determining interface dielectric losses in superconducting coplanar-waveguide resonators,” Phys. Rev. Appl. 12 (1), 014012 (2019)
[^Nersisyan2019]: Nersisyan, A., Poletto, S., Alidoust, N., Manenti, R., Renzas, R., Bui, C., Vu, K., Whyland, T., Mohan, Y., Sete, E. A. et al., “Manufacturing low dissipation superconducting quantum processors,” in 2019 IEEE International Electron Devices Meeting (IEDM), San Francisco, CA, 2019, pp. 31.1.1–31.1.4
[^Lock2019]: Lock, E. H., Xu, P., Kohler, T., Camacho, L., Prestigiacomo, J., Rosen, Y. J., and Osborn, K. D., “Using surface engineering to modulate superconducting coplanar microwave resonator performance,” IEEE Trans. Appl. Supercond. 29, 1700108 (2019).
[^Gao2021]: Gao, R., Yu, W., Deng, H., Ku, H.-S., Li, Z., Wang, M., … Deng, C. (2021). Epitaxial titanium nitride microwave resonators: Structural, chemical, electrical, and microwave properties. http://arxiv.org/abs/2111.04227
[^Kowsari2021]: Kowsari, D., Zheng, K., Monroe, J. T., Thobaben, N. J., Du, X., Harrington, P. M., … Murch, K. W. Fabrication and surface treatment of electron-beam evaporated niobium for low-loss coplanar waveguide resonators. Applied Physics Letters, 119 (13), 132601 (2021).
[^Degnan2022]: Degnan, Z., He, X., Frieiro, A. G., Sachkou, Y. P., Fedorov, A., & Jacobson, P. (2022). Ternary Metal Oxide Substrates for Superconducting Circuits. http://arxiv.org/abs/2201.06228
[^Zheng2022]: Zheng, K., Kowsari, D., Thobaben, N. J., Du, X., Song, X., Ran, S., … Murch, K. W. (2022). Nitrogen Plasma Passivated Niobium Resonators for Superconducting Quantum Circuits. http://arxiv.org/abs/2201.01776
[^Kim2021]: Kim, S., Terai, H., Yamashita, T., Qiu, W., Fuse, T., Yoshihara, F., … Semba, K. Enhanced-coherence all-nitride superconducting qubit epitaxially grown on Si Substrate. Communications Materials 2, 98 (2021)
[^Kopas2021]: Kopas, C. J., Gonzales, J., Zhang, S. , Queen, D. R., Wagner, B., Robinson, M., Huffman, J., Newman, N., "Low microwave loss in deposited Si and Ge thin-film dielectrics at single-photon power and low temperatures." AIP Advances 11, 095007 (2021). https://doi.org/10.1063/5.0041525
[^Buijtendorp2021]: Buijtendorp, B. T., Vollebregt, S., Karatsu, K., Thoen, D. J., Murugesan, V., Kouwenhoven, K., … Endo, A. Hydrogenated Amorphous Silicon Carbide: A Low-loss Deposited Dielectric for Microwave to Submillimeter Wave Superconducting Circuits (2021). http://arxiv.org/abs/2110.03500 
[^Hahnle2021]: Hahnle, S., Kouwenhoven, K., Buijtendorp, B., Endo, A., Karatsu, K., Thoen, D. J., … Baselmans, J. J. A. Superconducting Microstrip Losses at Microwave and Submillimeter Wavelengths. Physical Review Applied 16, 014019 (2021).
[^Phan2021]: Phan, D., Senior, J., Ghazaryan, A., Hatefipour, M., Strickland, W. M., Shabani, J., … Higginbotham, A. P. Detecting induced $p \pm ip$ pairing at the Al-InAs interface with a quantum microwave circuit (2021).  http://arxiv.org/abs/2107.03695
