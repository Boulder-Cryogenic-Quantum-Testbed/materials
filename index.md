---
layout: default
---

![Untitled design (1)](https://github.com/Boulder-Cryogenic-Quantum-Testbed/materials/assets/120617602/bd009e2b-24e2-44fb-88ea-db16635423d5)

* * *
 Superconducting qubits are coherence-limited by materials losses, but the lack of comparable interlaboratory metrics is stunting progress towards lower loss devices. Here, we compile resonator loss measurements from literature and attempt to compare them by scaling loss by the gap of the coplanar waveguide resonator to account for participation of the lossy material. This resource is intended for use by researchers interested in building higher performance materials stacks for superconducting quantum devices. This resource is based on information originally collected for:<br>
C. R. H. McRae, H. Wang, J. Gao, M. Vissers, T. Brecht, A. Dunsworth, D. Pappas, and J. Mutus, *Materials Loss Measurements Using Superconducting Microwave Resonators,* **091101**, (2020).[ *View Reference*](https://pubs.aip.org/aip/rsi/article/91/9/091101/906092/Materials-loss-measurements-using-superconducting)
<br>
# CPW Resonator Loss 
<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plotly.com/~crmcrae/4.embed?link=false" height="525" width="100%"></iframe>
<!--<img src="https://github.com/Boulder-Cryogenic-Quantum-Testbed/materials/assets/120617602/c78f15c2-9163-4332-8cfa-3215129dbd24"  width="615" height="45"-->
 ![New plotly symbol legend smaller](https://github.com/Boulder-Cryogenic-Quantum-Testbed/materials/assets/120617602/3cacc505-2df7-4eb6-85bb-8ffbfdcc2fd8)

<br>**Background diagonal lines represent constant interface losses with varying geometry while accounting for the filling factor of the TLS-ridden materials.**
<br>
<br>
# Dataset
* * *
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
<!--| SC    | Reference                | Dep.	         |Substrate	 | δLP      | Fδ0TLS   |  g (µm) |
|:------|:-------------------------|:--------------|:----------|:---------|:---------|:--------|
| Nb    |	Gao et al. (2008c)	     | Not Specified | Al2O3     |          | 2.40E-06 | 33      |
| Nb    |	Kumar et al. (2008)	     | Not Specified | Si		     |          | 2.94E-05 | 1       |
| Re    |	Wang et al. (2009)       | E-beam	       | Al2O3     | 1.00E-06	|	         | 6.4     |
| Al    |	Wang et al. (2009)	     | Sputter	     | Al2O3     | 3.00E-06	|	         | 6.4     |
| NbTiN |	Barends et al. (2010)	   | Sputter       | Si	       | 3.00E-06	|	         | 2       |
| Ta    |	Barends et al. (2010)	   | Sputter	     | Si	       | 3.00E-05	|	         | 2       |
| Nb    |	Macha et al. (2010)	     | Not Specified | Al2O3     |          | 2.40E-06 | 30      |
| Nb    |	Macha et al. (2010)	     | Not Specified | Si        |          | 1.30E-06 | 30      |
| Al    |	Macha et al. (2010)      | Not Specified | Al2O3     |          | 2.00E-06 | 30      |
| TiN   |	Vissers et al. (2010)    | Sputter	     | Al2O3     | 3.00E-05	|          | 2       |
| TiN   |	Vissers et al. (2010)	   | Sputter	     | Al2O3     | 2.00E-05	|	         | 2       |
|TiN    | Vissers et al. (2010)	   | Sputter	     | Al2O3     | 1.00E-05	|	         | 2       |
| TiN   |	Vissers et al. (2010)	   | Sputter	     | Si	       | 2.00E-06	|          | 2       |
| Nb    |	Wisbey et al. (2010)	   | Not Specified | Si		     |          | 1.30E-05 | 2       |
| Nb    | Wisbey et al. (2010)	   | Not Specified | Si		     |          | 7.00E-06 | 2       |
| Nb    |	Sage et al. (2011)	     | Sputter       | Si		     |          | 1.50E-05 | 5       |
| Nb	  | Sage et al. (2011)	     | Sputter	     | Al2O3     |          | 1.80E-05 | 5       |
| Al	  | Sage et al. (2011)	     | Sputter	     | Si		     |          | 1.50E-06 | 5       |
| Al	  | Sage et al. (2011)	     | Sputter	     | Al2O3     |          | 1.60E-06 | 5       |
| Al	  | Sage et al. (2011)	     | MBE	         | Al2O3     |          | 1.80E-06 | 5       |
| Re	  | Sage et al. (2011)	     | MBE	         | Al2O3     |          | 1.80E-06 | 5       |
| TiN	  | Sage et al. (2011)	     | Sputter	     | Si		     |          | 9.60E-07 | 5       |
| Al	  | Megrant et al. (2012)	   | Sputter       | Al2O3     | 2.50E-06	|          | 2       |
| Al	  | Megrant et al. (2012)	   | E-beam        | Al2O3     | 1.40E-06	|	         | 2       |
| Al	  | Megrant et al. (2012)	   | MBE           | Al2O3     | 5.80E-07	|	         | 2       |
| TiN	  | Ohya et al. (2013)	     | Sputter	     | Si	       | 1.00E-06	|          | 10      |
| Nb	  | Goetz et al. (2016) 	   | Sputter	     | Si	       |          | 9.00E-07 | 12      |
| Nb	  | Goetz et al. (2016)	     | Sputter	     | Al2O3     |          | 1.60E-06 | 12      |
| Al	  | Richardson et al. (2016) |	MBE	         | Si		     |          | 2.00E-07 | 12      |
| Al	  | Richardson et al. (2016) |	MBE	         | Si		     |          | 5.00E-07 | 12      |
| Al	  | Richardson et al. (2016) |	MBE	         | Al2O3     |          | 5.00E-07 | 12      |
| Al	  | Richardson et al. (2016) |	MBE	         | Al2O3     |          | 4.00E-07 | 2       |
| NbN	  | De Graaf et al. (2018)	 | Sputter	     | Al2O3     |          | 1.04E-05 | 2       |
| NbN	  | De Graaf et al. (2018)	 | Sputter	     | Al2O3     |          | 7.44E-06 | 2       |
| TiN	  | Calusine et al. (2018)	 | Sputter	     | Si        |          | 3.00E-07 | 11      |
| Al	  | Earnest et al. (2018)	   | E-beam        | Si	       | 3.10E-06 |	3.27E-06 | 9       |
| Al	  | Earnest et al. (2018)	   | E-beam	       | Si	       | 1.90E-06	| 1.53E-06 | 9       |
| Al	  | Earnest et al. (2018)	   | E-beam	       | Si	       | 1.80E-06	| 1.56E-06 | 9       |
| Al	  | Earnest et al. (2018)	   | E-beam	       | Si	       | 1.20E-06	| 8.00E-07 | 9       |
| In	  | McRae et al. (2018)	     | Therm. Evap.	 | Si		     |          | 4.00E-05 | 6       |
| In	  | McRae et al. (2018)	     | Therm. Evap.	 | Si		     |          | 5.00E-05 | 6       |
| TiN	  | Lock et al. (2019)	     | Sputter	     | Si		     |          | 2.00E-07 | 12      |
| Nb	  | Kowsari et al. (2021)	   | E-beam	       | Si		     |          | 3.00E-07 | 2       |
| Nb	  | Zheng et al. (2022)	     | E-beam	       | Si		     |          | 2.90E-07 | 2       |
| TiN	  | Gao et al. (2022)	       | Sputter	     | Al2O3     |	        | 3.00E-07 | 6       |
| Ta	  | Shi et al. (2022)	       | Sputter	     | Al2O3     |	        | 1.00E-06 | 5       |
| Ta	  | Lozano et al. (2022)	   | Sputter	     | Si		     |          | 4.00E-07 | 4.5     |
| Ta	  | Lozano et al. (2022)	   | Sputter	     | Si		     |          | 1.00E-06 | 4.5     |-->


![image](https://github.com/DylanBlevins49/scresonators-lossdiagram/assets/120617602/05bd47ce-c54c-4d0d-9217-6b84f0aad62a)

<br>
<br>
# References
* * *
<br>
Calusine, G., Melville, A., Woods, W., Das, R., Stull, C., Bolkhovsky, V., Braje, D., Hover, D., Kim, D. K., Miloshi, X. et al., "*Analysis and mitigation of interface losses in trenched superconducting coplanar waveguide resonators*" Appl. Phys. Lett. **112**, 062601 (2018).<a href="https://pubs.aip.org/aip/apl/article/112/6/062601/35936/Analysis-and-mitigation-of-interface-losses-in" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

De Graaf, S., Faoro, L., Burnett, J., Adamyan, A., Tzalenchuk, A. Y., Kubatkin, S., Lindström, T., and Danilov, A., “*Suppression of low-frequency charge noise in superconducting resonators by surface spin desorption*”, Nat. Commun. **9**, 1143 (2018).<a href="https://www.nature.com/articles/s41467-018-03577-2" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Earnest, C. T., Béjanin, J. H., McConkey, T. G., Peters, E. A., Korinek, A., Yuan, H., and Mariantoni, M., “*Substrate surface engineering for high-quality silicon/aluminium superconducting resonators,*” Supercond. Sci. Technol. **31**, 125013 (2018).<a href="https://arxiv.org/abs/1807.08072" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Gao, R., Yu, W., Deng, H., Ku, H.-S., Zhisheng, L., Wang, M., Miao, X., Lin, Y., & Deng, C. (2022). "*Epitaxial titanium nitride microwave resonators: Structural, chemical, electrical, and microwave properties,*" **6(3)**.<a href="https://arxiv.org/abs/2111.04227" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Goetz, J., Deppe, F., Haeberlein, M., Wulschner, F., Zollitsch, C. W., Meier, S., Fischer, M., Eder, P., Xie, E., Fedorov, K. G. et al., “*Loss mechanisms in superconducting thin film microwave resonators,*” J. Appl. Phys. **119**, 015304 (2016).<a href="https://pubs.aip.org/aip/jap/article-abstract/119/1/015304/141819/Loss-mechanisms-in-superconducting-thin-film?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Kowsari, D., K. Zheng, J. T. Monroe, N. J. Thobaben, X. Du, P. M. Harrington, E. A. Henriksen, D. S. Wisbey, K. W. Murch; "*Fabrication and surface treatment of electron-beam evaporated niobium for low-loss coplanar waveguide resonators,*" Appl. Phys. Lett. **27** , September 2021; 119 (13): 132601.<a href="https://pubs.aip.org/aip/apl/article/119/13/132601/40997/Fabrication-and-surface-treatment-of-electron-beam" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Kumar, S., Gao, J., Zmuidzinas, J., Mazin, B. A., LeDuc, H. G., and Day, P. K., “*Temperature dependence of the frequency and noise of superconducting coplanar waveguide resonators,*” Appl. Phys. Lett. **92(12)**, 123503 (2008).<a href="https://pubs.aip.org/aip/apl/article-abstract/92/12/123503/334498/Temperature-dependence-of-the-frequency-and-noise?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Lock, E. H., Xu, P., Kohler, T., Camacho, L., Prestigiacomo, J., Rosen, Y. J., and Osborn, K. D., “*Using surface engineering to modulate superconducting coplanar microwave resonator performance,*” IEEE Trans. Appl. Supercond. **29**, 1700108 (2019).<a href="https://ieeexplore.ieee.org/document/8606149" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Lozano, D. P., M. Mongillo , X. Piao , S. Couet , D. Wan , Y. Canvel , A. M. Vadiraj , Ts. Ivanov, J. Verjauw, R. Acharya, J. Van Damme, F. A. Mohiyaddin, J. Jussot, P. P. Gowda, A. Pacco, B. Raes, J. Van de Vondel, I. P. Radu, B. Govoreanu1 J. Swerts, A. Potočnik, and K. De Greve, “*Manufacturing high-Q superconducting α-tantalum resonators on silicon wafers*”, (2023)<a href="https://arxiv.org/abs/2211.16437" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Macha, P., van Der Ploeg, S. H. W., Oelsner, G., Il’ichev, E., Meyer, H.-G., Wünsch, S., and Siegel, M., “*Losses in coplanar waveguide resonators at millikelvin temperatures,*” Appl. Phys. Lett. **96(6)**, 062503 (2010).<a href="https://pubs.aip.org/aip/apl/article-abstract/96/6/062503/167025/Losses-in-coplanar-waveguide-resonators-at?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

McRae, C. R. H., Béjanin, J. H., Earnest, C. T., McConkey, T. G., Rinehart, J. R., Deimert, C., Thomas, J. P., Wasilewski, Z. R., and Mariantoni, M., “*Thin film metrology and microwave loss characterization of indium and aluminum/indium superconducting planar resonators,*” J. Appl. Phys. **123(20)**, 205304 (2018).<a href="https://pubs.aip.org/aip/jap/article-abstract/123/20/205304/155631/Thin-film-metrology-and-microwave-loss?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference </i></a>.<br>

Megrant, A., Neill, C., Barends, R., Chiaro, B., Chen, Y., Feigl, L., Kelly, J., Lucero, E., Mariantoni, M., O’Malley, P. J. J. et al., “*Planar superconducting resonators with internal quality factors above one million,*” Appl. Phys. Lett. **100**, 113510 (2012).<a href="https://pubs.aip.org/aip/apl/article-abstract/100/11/113510/126200/Planar-superconducting-resonators-with-internal?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Ohya, S., Chiaro, B., Megrant, A., Neill, C., Barends, R., Chen, Y., Kelly, J., Low, D., Mutus, J., O’Malley, P. J. J. et al., “*Room temperature deposition of sputtered TiN films for superconducting coplanar waveguide resonators,*” Supercond. Sci. Technol. **27**, 015009 (2013).<a href="https://iopscience.iop.org/article/10.1088/0953-2048/27/1/015009/meta" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Richardson, C. J. K., Siwak, N. P., Hackley, J., Keane, Z. K., Robinson, J. E., Arey, B., Arslan, I., and Palmer, B. S., “*Fabrication artifacts and parallel loss channels in metamorphic epitaxial aluminum superconducting resonators,*” Supercond. Sci. Technol. **29**, 064003 (2016).<a href="https://iopscience.iop.org/article/10.1088/0953-2048/29/6/064003" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Sage, J. M., Bolkhovsky, V., Oliver, W. D., Turek, B., and Welander, P. B., “*Study of loss in superconducting coplanar waveguide resonators,*” J. Appl. Phys. **109**, 063915 (2011).<a href="https://pubs.aip.org/aip/jap/article-abstract/109/6/063915/989262/Study-of-loss-in-superconducting-coplanar?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Shi, Lili, Tingting Guo, Runfeng Su, Tianyuan Chi, Yifan Sheng, Junliang Jiang, Chunhai Cao, Jingbo Wu, Xuecou Tu, Guozhu Sun, Jian Chen, Peiheng Wu; "*Tantalum microwave resonators with ultra-high intrinsic quality factors,*" Appl. Phys. Lett. **12** , December 2022; 121 (24): 242601.<a href="https://pubs.aip.org/aip/apl/article-abstract/121/24/242601/2834741/Tantalum-microwave-resonators-with-ultra-high?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>. <br>

Vissers, M. R., Gao, J., Wisbey, D. S., Hite, D. A., Tsuei, C. C., Corcoles, A. D., Steffen, M., and Pappas, D. P., “*Low loss superconducting titanium nitride coplanar waveguide resonators,*” Appl. Phys. Lett. **97**, 232509 (2010).<a href="https://pubs.aip.org/aip/apl/article-abstract/97/23/232509/325118/Low-loss-superconducting-titanium-nitride-coplanar?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Vissers, M.R., J. Gao, D. S. Wisbey, D. A. Hite, C. C. Tsuei, A. D. Corcoles, M. Steffen, D. P. Pappas; "*Low loss superconducting titanium nitride coplanar waveguide resonators,*" Appl. Phys. Lett. **6** , December 2010; 97 (23): 232509. <a href="https://pubs.aip.org/aip/apl/article-abstract/97/23/232509/325118/Low-loss-superconducting-titanium-nitride-coplanar?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Wang, H., Hofheinz, M., Wenner, J., Ansmann, M., Bialczak, R. C., Lenander, M., Lucero, E., Neeley, M., O’Connell, A. D., Sank, D. et al., “*Improving the coherence time of superconducting coplanar resonators,*” Appl. Phys. Lett. **95**, 233508 (2009).<a href="https://pubs.aip.org/aip/apl/article-abstract/95/23/233508/120944/Improving-the-coherence-time-of-superconducting?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Wisbey, D. S., Gao, J., Vissers, M. R., da Silva, F. C. S., Kline, J. S., Vale, L., and Pappas, D. P., “*Effect of metal/substrate interfaces on radio-frequency loss in superconducting coplanar waveguides,*” J. Appl. Phys. **108**, 093918 (2010).<a href="https://pubs.aip.org/aip/jap/article-abstract/108/9/093918/345430/Effect-of-metal-substrate-interfaces-on-radio?redirectedFrom=fulltext" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>

Zheng K., D. Kowsari, N. J. Thobaben, X. Du, X. Song, S. Ran, E. A. Henriksen, D. S. Wisbey, K. W. Murch; "*Nitrogen plasma passivated niobium resonators for superconducting quantum circuits,*" Appl. Phys. Lett. **7** , March 2022; 120 (10): 102601.<a href="https://pubs.aip.org/aip/apl/article/120/10/102601/2833153/Nitrogen-plasma-passivated-niobium-resonators-for" target="_blank" rel="noopener noreferrer"><i> View Reference</i></a>.<br>
<br>
<br>
<br>
<br>
* * *
### Relevant Links 
- [**McRae Lab Website**](https://www.colorado.edu/lab/mcrae/)
- [**BCQT Project Website**](https://www.nist.gov/programs-projects/boulder-cryogenic-quantum-testbed)
- [**BCQT GitHub Page**](https://github.com/Boulder-Cryogenic-Quantum-Testbed)<br>
![NOBG BCQT](https://github.com/DylanBlevins49/scresonators-lossdiagram/assets/120617602/e5a4fb56-1025-429b-b335-473f7bfc9f6b)<br><br>
<center>To suggest a reference to be added, please email <b>coreyrae.mcrae@colorado.edu.</b></center>


