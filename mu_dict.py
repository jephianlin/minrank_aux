print "---get_mu_from_dict, has_minor, find_mu, etc."

## mu_dict contains graph6.string and it mu for graphs with at most 7 vertices.
mu_dict={'FG_qw': 2, 'F@HI_': 2, 'F_LLg': 3, 'F?]rw': 3, 'FG?yo': 3, 'FR\\}w':
4, 'FG]^g': 3, 'FGD\\o': 3, 'ENzw': 4, 'FHQ?w': 2, 'F?\\~_': 4, 'FB]uW':
3, 'FGCWw': 3, 'F?Dlw': 2, 'F@Fmw': 3, 'F`L|w': 4, 'FPLYw': 3, 'FA]rw':
3, 'F@\\zw': 4, 'FKNJw': 3, 'F@Q?w': 2, 'F?^~w': 4, 'FNz~w': 5, 'F?F~o':
3, 'FLr@w': 4, 'FJ]~w': 4, 'F`L~w': 4, 'F@\\cg': 3, 'FNz~o': 4, 'FOTPw':
3, 'FY_}w': 3, 'F`L|o': 4, 'F?\\~w': 4, '@': 0, 'E@FG': 2, 'F?LZw': 3,
'FJenw': 3, 'EInw': 3, 'E_Nw': 2, 'DJ[': 3, 'FjaHw': 3, 'FGC^w': 3,
'F@NMg': 3, 'F_Cxw': 3, 'F??Ww': 2, 'FC\\zw': 4, 'F@^~o': 4, 'EJmw': 3,
'F_Cxo': 3, 'F??Wo': 2, 'F??yo': 2, 'F?StG': 2, 'F@LAG': 2, 'FIc~G': 3,
'EIno': 3, 'F?LZW': 2, 'FAEhw': 2, 'FK~~w': 4, 'F@]eg': 3, 'DJ{': 3,
'F?LZ_': 3, 'FGC^W': 2, 'F?Dzo': 3, 'F?]Rg': 3, 'F_@|w': 3, 'DJk': 2,
'FCDjW': 3, 'FGC^G': 2, 'F@Tzo': 3, 'F@huw': 3, 'FAChW': 2, 'FJY}o': 3,
'E?@w': 2, 'FLv~o': 4, 'F?N~o': 3, 'F?`zo': 3, 'ER^W': 3, 'FPT^w': 3,
'D]{': 3, 'F?Cfw': 2, 'F?L~w': 3, 'FBnvO': 4, 'EFzw': 4, 'FJY\\w': 3,
'EHUW': 2, 'Flp|w': 4, 'FAKzW': 3, 'FG?yw': 3, 'FJ?KW': 2, 'F??Jg': 2,
'F?L^W': 2, 'F?N~w': 3, 'FBnfw': 4, 'F?`zw': 3, 'FC\\~W': 4, 'E?N?': 1,
'FBn~o': 4, 'FFzbw': 4, 'F@\\vw': 4, 'F`H[w': 3, 'F`K}W': 3, 'F@Q@w': 2,
'F_Kpw': 3, 'F@Fmo': 3, 'F@_zw': 3, 'F@Tfw': 3, 'FI\\|w': 4, 'FJY^w': 4,
'F?L~o': 3, 'EFz_': 4, 'FI]|w': 4, 'F@Lmw': 3, 'FAY|o': 3, 'F?Fnw': 3,
'FB]|w': 4, 'E@Pw': 2, 'ECXw': 2, 'FJn^W': 3, 'E?NW': 2, 'FB_zW': 3,
'F??Bw': 2, 'FBnvW': 4, 'FFzfw': 5, 'F?K}_': 2, 'FJ]|w': 4, 'F?B~o': 3,
'E?NG': 2, 'FT\\uW': 4, 'F?N^W': 3, 'F?L|w': 3, 'FJ]^G': 4, 'F?G]w': 2,
'F@R~w': 3, 'FGnRw': 3, 'E?Nw': 2, 'Fbc~W': 3, 'FA_xw': 3, 'FDp~o': 3,
'F_CXw': 3, 'F_Dlw': 3, 'FK\\~w': 4, 'FBn^w': 3, 'FEW~W': 3, 'FFYmw': 3,
'FBY}o': 3, 'FBNmw': 3, 'FB^dw': 4, 'FA_pW': 2, 'F?N^w': 3, 'FB^~o': 4,
'EK]w': 2, 'E_Kw': 2, 'F@Dmw': 3, 'FI_xw': 3, 'FBebW': 3, 'F?CPW': 2,
'F?L^?': 2, 'FGCZG': 2, 'F`Gyw': 3, 'FwCWw': 3, 'F_]~w': 4, 'F@Pzo': 3,
'E@Lw': 3, 'F@?}W': 2, 'FKdjg': 3, 'FGCZW': 2, 'E_Ko': 2, 'F?\\~g': 4,
'FBZDw': 3, 'F@J^w': 3, 'FB?KW': 2, 'F@~uw': 4, 'F@O[w': 2, 'FI?XW': 2,
'FHL[w': 3, 'F@L|o': 3, 'F?opw': 2, 'F@UZw': 3, 'F?Lkw': 2, 'FGEZw': 3,
'E@LW': 2, 'F@ozg': 3, 'FL]uW': 3, 'F]~vw': 4, 'FBn~w': 4, 'FGEZo': 2,
'F@?}O': 2, 'F?opg': 2, 'F`?XW': 2, 'F@FJw': 2, 'FBY~w': 4, 'F?^~o': 4,
'F@?]W': 2, 'F@H]w': 3, 'F?drW': 3, 'F?F~w': 3, 'FIQ|w': 4, 'E?Fg': 2,
'FGc~w': 3, 'F_opw': 2, 'F??}w': 2, 'FB]~w': 4, 'F?D~o': 3, 'F`]~_': 4,
'FB_mw': 2, 'EHuw': 3, 'FKNmw': 3, 'F??}o': 2, 'FD`jw': 3, 'F?D~w': 3,
'F@?]O': 2, 'FAN@w': 2, 'FIQ|o': 4, 'F@PDw': 2, 'F`Maw': 3, 'F?drw': 3,
'FGeZ_': 2, 'DF{': 3, 'F@O\\G': 2, 'F?D@w': 2, 'DFw': 3, 'F?@~o': 3,
'FPvZw': 4, 'F??}W': 2, 'FAd|o': 3, 'F?D~O': 3, 'FOLQw': 2, 'F?@~w': 3,
'F??}O': 2, 'F?D~W': 3, 'EI_w': 2, 'FJAKO': 2, 'F@U^w': 3, 'F@fbo': 3,
'F@H?w': 2, 'F?L^G': 2, 'F?~v_': 4, 'FINLw': 4, 'F_?Xw': 2, 'FJaHw': 2,
'F@TTW': 3, 'F`?Gw': 2, 'F??yw': 2, 'F??Z?': 1, 'FIAHo': 2, 'E?Dw': 2,
'F`t|w': 3, 'FHd\\w': 3, 'FBY^?': 4, 'F@\\rw': 4, 'FK\\|w': 3, 'FBj@w':
3, 'F@Xsw': 3, 'F_?Xo': 2, 'FBUlW': 3, 'EF~w': 4, 'F??xo': 3, 'F`G]w':
3, 'E?Dg': 2, 'EB~o': 3, 'F@N^W': 3, 'F_?XW': 2, 'FA\\tw': 3, 'F@T~w':
3, 'FKNNw': 3, 'Fb]lg': 3, 'F?WZg': 3, 'FAIXw': 2, 'E_]o': 3, 'F?Cyw':
3, 'F@R@o': 2, 'F?Krw': 3, 'FJQLw': 3, 'E_]w': 3, 'F?Cyo': 2, 'F??Fw':
2, 'FLp|w': 4, 'E?Ko': 2, 'EHQW': 2, 'F?StW': 2, 'F@Tbw': 3, 'FoL^w': 3,
'EJ^w': 4, 'FWD[o': 3, 'FHU}w': 4, 'FWCYw': 3, 'FIe`w': 3, 'E@~w': 3,
'FGLSW': 3, 'E?Kw': 2, 'E@~o': 3, 'FBXcw': 4, 'E^~w': 4, 'FC^bw': 4,
'FG_yw': 3, 'FIMmw': 3, 'FCdzo': 3, 'F?]}w': 3, 'F?\\tw': 3, 'F@Kxw': 4,
'FJ\\~w': 5, 'F?LPw': 2, 'FKLkw': 2, 'FB`kw': 3, 'FC^vW': 4, 'F?Kyw': 3,
'F?Uro': 2, 'F@AJo': 2, 'FJvdw': 3, 'F@HSW': 2, 'FGG[w': 2, 'FGLSw': 3,
'FoCiw': 2, 'F@HSO': 1, 'FAS|w': 3, 'F?\\t_': 3, 'F@p|w': 3, 'FBd~W': 4,
'Fbg}w': 3, 'FI]\\g': 3, 'F_N~w': 3, 'F@\\sw': 3, 'F@ptw': 3, 'FEXlw':
3, 'F??zw': 3, 'F?^vw': 4, 'Ftpzw': 4, 'FBZ@w': 3, 'FCdj_': 3, 'FA_~o':
3, 'DK[': 2, 'F@Diw': 3, 'F@NNg': 3, 'F?v`w': 3, 'FDO~W': 3, 'FGd~_': 3,
'F@?XW': 2, 'F??zo': 3, 'F`FHw': 2, 'EI]w': 3, 'FHu~w': 4, 'FCXPW': 2,
'F_?xw': 3, 'Fs\\~w': 5, 'FBY~o': 4, 'F@FNw': 3, 'F`Oxw': 3, 'F?YPw': 2,
'DK{': 2, 'FBh|w': 3, 'F_Kzw': 3, 'F@Q^w': 3, 'FaM~w': 3, 'F@U^W': 3,
'FAMRW': 3, 'F_?xo': 3, 'F??GW': 2, 'E@HW': 2, 'F@o~g': 3, 'FR^^w': 4,
'FGd~w': 3, 'F_KuW': 3, 'DBk': 2, 'EN~w': 4, 'E@^W': 2, 'E?]o': 2,
'F@Q}w': 3, 'DBg': 1, 'EB~w': 3, 'DB{': 2, 'FHUZw': 3, 'E?]w': 2,
'EL~w': 3, 'F@LIg': 2, 'EB^w': 3, 'FK\\zw': 4, 'FBMmW': 3, 'EJeg': 2,
'F@U^?': 3, 'EJ~w': 4, 'FGLZw': 3, 'F@QGw': 2, 'F@Tzw': 3, 'F?L}w': 3,
'F?@zo': 3, 'FK`_w': 2, 'E@^w': 3, 'FHQZw': 3, 'FDhaw': 3, 'FsLZW': 3,
'FAK~W': 3, 'DB[': 2, 'FJ_}W': 3, 'FGU|w': 3, 'FBX|w': 4, 'FPTZw': 3,
'F@K~w': 4, 'EJ~o': 4, 'F?_yo': 2, 'FJQHw': 3, 'FIS|W': 3, 'DBW': 2,
'F?@zw': 3, 'F@H\\w': 3, 'F??^w': 2, 'FODZo': 3, 'F??ZW': 2, 'F@QHw': 2,
'F@?GW': 2, 'FGK]G': 2, 'FFz~w': 5, 'F@LSW': 2, 'F?B~w': 3, 'F?C^?': 2,
'FGezw': 3, 'EA]o': 2, 'FZn]w': 4, 'F@Lew': 3, 'F??ZG': 2, 'FGN^w': 3,
'FwC}w': 3, 'FkYXw': 3, 'FODZw': 3, 'F`Lkw': 3, 'F?~vw': 4, 'F@X\\g': 3,
'F??Zw': 2, 'F@YPw': 2, 'FGL^w': 3, 'F_N~o': 3, 'Fo^Pw': 3, 'Fdhzw': 4,
'FKcqW': 2, 'FKG]W': 2, 'F@Lzw': 4, 'FbY|o': 4, 'F?K~w': 3, 'FJYKg': 3,
'FCX~w': 3, 'F`NNw': 3, 'F?C^w': 3, 'Fo?yo': 3, 'FG??w': 2, 'FI?\\W': 2,
'Fo?yw': 3, 'F`l~g': 4, 'Fb]|w': 4, 'FLvfw': 4, 'F@]vw': 3, 'FJY}w': 3,
'FI~tw': 4, 'FHOyw': 3, 'F@@Gw': 2, 'F_K^G': 2, 'Dbk': 2, 'F?C^W': 2,
'F`]rw': 4, 'FSOzw': 3, 'F@nRw': 3, 'F@QZo': 2, 'DLo': 2, 'F_S|w': 3,
'F@Tcw': 3, 'E`Lw': 3, 'FK^~w': 4, 'FKL^W': 3, 'F?C^G': 2, 'F?NVW': 3,
'FL~vw': 4, 'FK?}O': 3, 'DL{': 2, 'F?Dkw': 2, 'FHQZo': 3, 'FG\\sw': 3,
'F@P|o': 3, 'F@^vo': 4, 'EGcw': 2, 'FALlw': 3, 'F@dzw': 3, 'EJaG': 2,
'F`K~w': 4, 'FKdzw': 3, 'F@NBw': 3, 'F_|tg': 4, 'FEXhw': 3, 'FLpzw': 4,
'FG[}g': 3, 'F??Jw': 2, 'FHU^?': 3, 'F@P|w': 3, 'FM`hw': 3, 'FB\\|w': 4,
'F?Chw': 2, 'F_L|w': 3, 'F_?~w': 3, 'E@]w': 3, 'FK_yo': 3, 'FG?Gw': 2,
'F@@kw': 2, 'F?Dnw': 3, 'F@l~g': 4, 'FBY^w': 4, 'F@@ko': 2, 'F?\\zw': 4,
'F@\\|w': 4, 'E@ow': 2, 'F?Ch_': 2, 'F?oow': 2, 'F`]~w': 4, 'F@nBg': 3,
'E@]o': 2, 'FJ\\|w': 4, 'EBYW': 3, 'F@QZw': 2, 'F@Ozw': 3, 'ELrw': 3,
'Es\\w': 4, 'EBZw': 3, 'FImvw': 4, 'FGC{o': 2, 'FQ\\sw': 3, 'F`K}w': 3,
'FF^nW': 4, 'FG?Gg': 1, 'D^{': 3, 'FaG{w': 2, 'FHeZw': 3, 'FIOxw': 4,
'F@Neo': 3, 'F@OsW': 2, 'F?C~O': 2, 'EBhw': 2, 'FHU^w': 3, 'F`\\|w': 4,
'F?L^_': 3, 'FHQ^o': 3, 'F?C~w': 3, 'F@K}w': 3, 'FCLZW': 2, 'F?W^g': 3,
'FJd~W': 4, 'FOLYw': 3, 'FWCWw': 3, 'F`Lzw': 4, 'EGLW': 2, 'FIo|g': 4,
'D@O': 1, 'F@Q}o': 3, 'FGdzw': 3, 'FELlW': 3, 'FJm~w': 4, 'FHQ^w': 3,
'F?C~o': 3, 'FImrw': 4, 'F`H\\w': 3, 'EJ]w': 3, 'F??^o': 2, 'FB]^G': 4,
'EGCW': 2, 'F@]uW': 3, 'FBY^G': 4, 'F?CZW': 2, 'FAmrw': 3, 'FBj^w': 3,
'FADlW': 2, 'F?C~W': 2, 'FBnbw': 4, 'F?Djw': 3, 'FK?}W': 3, 'F@Law': 3,
'F??^G': 2, 'E@vw': 3, 'FGdrw': 3, 'F?CqW': 2, 'FB`lw': 3, 'F?Kzw': 3,
'F`N@w': 3, 'FFo~W': 4, 'F@]uw': 3, 'F_L|o': 3, 'F@CiW': 2, 'FK]~w': 3,
'F?\\|w': 3, 'F`L~o': 4, 'FHd}w': 3, 'FGDkw': 2, 'F?CqO': 1, 'F@Tj_': 3,
'FLvbw': 4, 'F?NJw': 3, 'FHFKw': 3, 'F_C~w': 3, 'EK^w': 3, 'F?[uG': 3,
'FHO}w': 3, 'F@@Kw': 2, 'FGC\\w': 3, 'F?Dcw': 2, 'F`N^W': 3, 'F@OZG': 2,
'F`N~o': 4, 'FIdtW': 3, 'E@Ow': 2, 'F??^?': 2, 'F?CZw': 3, 'FK`zo': 3,
'F?~vg': 4, 'FGAZo': 2, 'F@qZw': 2, 'FBY}w': 3, 'FGc}_': 3, 'FSTjw': 3,
'F@\\}w': 3, 'F_C~W': 2, 'FJ^~o': 5, 'FBO|W': 3, 'F??~o': 3, 'F`Kyw': 3,
'FGC\\W': 2, 'E]~w': 4, 'F?DcW': 2, 'F_oxw': 3, 'D~{': 4, 'F??~w': 3,
'FKcyw': 3, 'E]~o': 3, 'E~~w': 5, 'FDprW': 3, 'F?CJG': 2, 'FoNZw': 3,
'F?CZ?': 2, 'FI`|w': 3, 'F@T|w': 3, 'E?^o': 3, 'FAgzg': 2, 'E`]w': 3,
'F?s~g': 3, 'F?@|w': 3, 'F@Maw': 3, 'F@P~w': 3, 'E@YW': 2, 'F?@|o': 3,
'FB]~W': 4, 'F@KuW': 3, 'Fkoxw': 4, 'F@T|o': 3, 'E@YO': 1, 'E?^w': 3,
'FEG^W': 3, 'E`]o': 3, 'EB]w': 3, 'FGL}w': 3, 'FC\\vW': 4, 'F_Kvw': 3,
'F@H^o': 3, 'FI`|o': 3, 'F?C}w': 3, 'F@QFw': 2, 'F@N]w': 3, 'F@~vg': 4,
'FQT|o': 3, 'FJejw': 3, 'F@W}g': 3, 'F@H^w': 3, 'FGdvw': 3, 'F?L|o': 3,
'FD\\~W': 4, 'F`Kxw': 4, 'FIO|w': 4, 'E@Vw': 2, 'F@HYo': 3, 'F`Lzo': 4,
'E?LW': 2, 'F?Czo': 3, 'F@J]w': 3, 'F??@w': 2, 'F@Y^w': 3, 'F@O~w': 3,
'FB~~w': 4, 'F?Czw': 3, 'F@J]o': 3, 'F?Dzw': 3, 'E@`w': 2, 'F?O|g': 2,
'F_Ch_': 2, 'F??G_': 1, 'F_K}w': 3, 'FIAHw': 2, 'F@HYw': 3, 'F@o~w': 3,
'E?LO': 1, 'Ek]w': 3, 'FC\\~w': 4, 'F@Y^_': 3, 'F@S}W': 2, 'EK~w': 3,
'ELv_': 3, 'E?Lw': 2, 'FA_hw': 2, 'FAdl_': 3, 'FAK|W': 3, 'F??Gg': 1,
'F?CzW': 2, 'F@V~w': 3, 'FQT|w': 3, 'F@J^o': 3, 'FBX~w': 4, 'EK~o': 3,
'F_Chw': 2, 'F??Gw': 2, 'F@~~w': 4, 'FkUhw': 4, 'FGUPw': 2, 'F@IAw': 2,
'F?Cmg': 2, 'FKW}w': 3, 'F@HZw': 3, 'F?C_w': 2, 'FJ~vw': 5, 'FJaNw': 3,
'FAMjw': 3, 'F@L}o': 3, 'F@Umg': 3, 'FEHkw': 2, 'F?Kvw': 3, 'FHU^G': 3,
'F@`zw': 3, 'E?~o': 3, 'FQL}w': 3, 'F@P@w': 2, 'F@H}w': 3, 'FF`jW': 4,
'F_K~w': 3, 'F?lvg': 3, 'FHU}o': 4, 'F?^vo': 4, 'F@Okw': 2, 'F]p|w': 4,
'FAizo': 3, 'F?O|w': 3, 'FGCXw': 3, 'FLl}w': 4, 'E?~w': 3, 'F@Ujw': 3,
'F@CeW': 2, 'EIe_': 2, 'F@H}o': 3, 'FBy}w': 3, 'E@Kw': 3, 'F`N~w': 4,
'FICkW': 2, 'FGlug': 3, 'F?KuW': 3, 'FHQ}o': 3, 'FCLjw': 3, 'F?NNw': 3,
'FJn~o': 4, 'FK`~w': 3, 'F@o}w': 3, 'F@~vw': 4, 'FHQ}w': 3, 'FGEJg': 2,
'F?L\\g': 3, 'FJn~w': 4, 'FK`~o': 3, 'F@]~w': 4, 'FIa@w': 2, 'F@O^G': 2,
'FB]lg': 3, 'Fo\\sw': 4, 'F?NN_': 3, 'FBYZw': 4, 'FJ~~w': 5, 'FGd~g': 3,
'F?L\\_': 2, 'FBXzw': 4, 'F?CmW': 2, 'F@d~o': 3, 'Fo?Zw': 2, 'F?D|o': 3,
'F@NFw': 3, 'FIl~g': 4, 'F_YPw': 2, 'F@KqW': 3, 'F`?}W': 2, 'F@Y]w': 3,
'FCHJw': 2, 'F@Oyw': 2, 'E?Bw': 2, 'F@UuW': 2, 'EBYw': 3, 'F@HZo': 3,
'FeK~W': 3, 'FICcW': 2, 'F_Krw': 3, 'F?Oxw': 3, 'F`MZw': 3, 'F@QBw': 2,
'FG?}o': 3, 'F@IZo': 3, 'F@\\tw': 4, 'F?]~w': 3, 'FTX}w': 3, 'F`CmW': 2,
'FDUbW': 3, 'F@LZW': 3, 'F?Cbw': 2, 'FBhzw': 3, 'FBXzo': 3, 'F?NNg': 3,
'F@?Mw': 2, 'D_K': 1, 'C?': 1, 'FK_qW': 2, 'F`]vw': 4, 'Fh_}w': 3,
'E@UW': 2, 'FI]~w': 4, 'F@Lkw': 3, 'FB]}w': 3, 'F????': 1, 'CK': 1,
'CJ': 2, 'F@OKg': 2, 'CN': 2, 'FJ^~w': 5, 'CL': 1, 'F@v~w': 4, 'CB': 1,
'F@t~g': 3, 'C@': 1, 'FG_Zg': 2, 'CF': 2, 'E@Rw': 2, 'F@L}w': 3, 'EJYW':
3, 'FG]}w': 3, 'FI_~w': 3, 'C^': 2, 'C]': 2, 'F???W': 1, 'FQdzw': 3,
'F?\\tg': 3, 'F?\\rw': 4, 'FIefw': 3, 'FBJKw': 3, 'FGEJw': 2, 'F`Dkw':
3, 'FbY\\w': 4, 'FGGYw': 2, 'FDdbW': 2, 'Fk?gw': 2, 'FTpzw': 4, 'F?svG':
3, 'F@]~_': 4, 'FA]~_': 3, 'F?Fno': 3, 'F_@|o': 3, 'F?\\r_': 4, 'FI}vg':
4, 'C~': 3, 'FJn^w': 4, 'F???w': 2, 'FHN]w': 4, 'FDhzw': 4, 'F??xw': 3,
'FK?GW': 2, 'F@]}w': 3, 'FB]vW': 3, 'F?CRW': 2, 'F@@Hw': 2, 'F??Hg': 2,
'F?D|w': 3, 'EJnw': 3, 'F@?ZW': 2, 'F?L^w': 3, 'Fjm~w': 5, 'F@@Ho': 2,
'EoLW': 2, 'FJY[w': 3, 'FXT[w': 4, 'E@Nw': 3, 'F?L[w': 3, 'F@h}o': 3,
'F@jRw': 3, 'E`Kw': 3, 'F_?Hg': 2, 'FAdtO': 2, 'FI_zw': 3, 'DIk': 2,
'F@CaW': 2, 'F@Pzw': 3, 'FGEXw': 3, 'FHLYw': 4, 'EJnW': 3, 'F_?Hw': 2,
'FCDnW': 3, 'FKL\\W': 3, 'F?NBw': 2, 'E@NW': 2, 'F?org': 2, 'F`?^W': 2,
'FBY|o': 4, 'EBn_': 3, 'FHQSO': 2, 'FC\\ng': 3, 'EGdw': 2, 'EBnW': 2,
'FGC}W': 2, 'FI\\tw': 3, 'F@Gyw': 3, 'F`Q@w': 2, 'Fbh|w': 4, 'F?~~w': 4,
'E@N?': 2, 'FHQ[w': 3, 'D@s': 2, 'EL~o': 3, 'F?MRw': 2, 'F?K}w': 3,
'FF~~w': 5, 'D@{': 2, 'EGdo': 2, 'E@\\w': 3, 'FIn~w': 4, 'F@LZw': 3,
'Fk]~w': 4, 'EBnw': 3, 'FGC}w': 3, 'F]~~w': 5, 'D@K': 2, 'F??Hw': 2,
'FFz~o': 4, 'FWN]w': 4, 'FN~~w': 5, 'FBh}w': 3, 'D@S': 1, 'F?C`w': 2,
'E@\\o': 3, 'FKzPw': 3, 'D@[': 2, 'F?CiW': 2, 'F@??W': 1, 'F?Kuw': 3,
'F??XW': 2, 'BG': 1, 'F?O|o': 3, 'EPTW': 2, 'FK~vw': 4, 'F_C_W': 1,
'F@K}W': 3, 'E??G': 1, 'FBj~o': 3, 'F`_zw': 3, 'FDx~g': 4, 'BW': 1,
'F@C]W': 2, 'F_]vw': 4, 'F@Vlw': 3, 'F@LYw': 3, 'FKHGw': 2, 'F??XO': 1,
'F?_rw': 2, 'E??W': 1, 'FG?}w': 3, 'F@T`w': 3, 'F??^W': 2, 'F??Xw': 2,
'F@YVw': 2, 'F_W\\g': 3, 'FB~vw': 4, 'E@QW': 2, 'F@G]G': 2, 'FIS|w': 4,
'FBZ~o': 4, 'F_YXw': 2, 'FK^~o': 4, 'F@N~w': 4, 'FHM]w': 3, 'FBZ~w': 4,
'Bw': 2, 'F?O|_': 2, 'FIU|o': 4, 'FCHiw': 2, 'FK~v_': 4, 'FG?Zw': 2,
'F?]~_': 3, 'E??w': 2, 'F@N~o': 4, 'FJ\\zw': 5, 'FLr~w': 4, 'F@L~w': 4,
'F?]uw': 3, 'FL~~w': 4, 'F`YPw': 3, 'F?\\vw': 4, 'FIebw': 3, 'F?Ku?': 2,
'EJ\\w': 4, 'F?LRW': 2, 'D`K': 2, 'F?Tto': 3, 'E@Q?': 1, 'F?NPw': 2,
'F@Tkw': 3, 'F_C`w': 2, 'FwL[w': 3, 'F@L~o': 4, 'FpL]w': 4, 'FB\\~w': 4,
'FAU`w': 2, 'FENnw': 4, 'FaG\\w': 2, 'FJaJw': 3, 'FAYPw': 2, 'FAG}w': 2,
'F@T\\W': 3, 'F?LRw': 2, 'FGG]w': 2, 'Fbh\\w': 4, 'FEOhW': 2, 'F?S|w':
3, 'FLp~w': 4, 'FKWyw': 3, 'E???': 1, 'Fbj@w': 3, 'F@NJw': 3, 'F@`Zw':
3, 'B?': 1, 'FU\\~W': 4, 'FClrw': 3, 'F?]u_': 3, 'FKK}W': 3, 'FpUZw': 4,
'F@N@w': 3, 'F?dzw': 3, 'FaK|W': 3, 'EImw': 3, 'F?^tw': 3, 'FBh~w': 3,
'F`G}w': 3, 'FK`zw': 3, 'F?Cnw': 2, 'FB^~w': 4, 'EImo': 3, 'F_GWw': 2,
'F@\\~_': 4, 'Fj]|w': 5, 'F@R~o': 3, 'F@?^W': 2, 'FAmzw': 3, 'FM^lw': 4,
'F@\\~g': 4, 'D??': 1, 'EG?W': 1, 'F?`rw': 3, 'E@^o': 3, 'F@h^g': 3,
'FoCyw': 3, 'F@\\~w': 4, 'F`KuW': 3, 'FHTcw': 3, 'FJYZw': 4, 'F@G}w': 3,
'F?K}W': 3, '?': -1, 'F?`ro': 3, 'Fk_zw': 4, 'D?[': 2, 'EB\\w': 3,
'F?CNG': 2, 'FKYZw': 3, 'EAMw': 2, 'F@N^o': 3, 'FAStW': 2, 'FIK}W': 4,
'FGCyo': 3, 'F@N^w': 3, 'D?K': 1, 'F@L^G': 3, 'FInvw': 4, 'EBjw': 2,
'FGCyw': 3, 'FG^Tw': 3, 'ELpw': 3, 'D?C': 1, 'E_?w': 2, 'F@]rw': 3,
'D?{': 2, 'F@L^w': 3, 'F@Vcw': 3, 'F@D^W': 3, 'F?W\\g': 2, 'F@N^O': 3,
'F?CeW': 2, 'FIm~w': 4, 'F?D_w': 2, 'E?Fw': 2, 'EBjW': 2, 'Fbn~w': 4,
'EK`w': 2, 'FHNMw': 3, 'FoCZW': 2, 'F@Tl_': 2, 'F@`~w': 3, 'Fw?Ww': 2,
'Ebnw': 3, 'EJqw': 3, 'F?Opw': 2, 'FPT}o': 3, 'F?Kqw': 3, 'FIejw': 3,
'FJQ\\O': 3, 'FJQ\\W': 3, 'F@Kyw': 3, 'F@CmW': 2, 'F?]vw': 3, 'FC\\rW':
3, 'F@`~o': 3, 'FGN\\w': 3, 'FoCZw': 3, 'F_Kxw': 3, 'F?Kxw': 3, 'FG?^w':
2, 'E_Cw': 2, 'F@Tlw': 3, 'F?KqW': 3, 'F@YRw': 2, 'F`C^W': 3, 'F?]v_':
3, 'FEGmw': 2, 'Fie`w': 3, 'F@Tdw': 3, 'E_Cg': 1, 'FA]vw': 3, 'FIM\\W':
3, 'F`IZo': 3, 'F@^^w': 3, 'EK\\w': 3, 'FHo}g': 3, 'FpLYw': 4, 'FB\\zw':
4, 'E`NG': 2, 'FGW[g': 2, 'F?CXw': 3, 'FGN^o': 3, 'F@~v_': 4, 'FGCZw':
3, 'FGAZw': 2, 'F@^vw': 4, 'F@P~o': 3, 'F@Lzo': 4, 'F?LVw': 2, 'F@L[w':
3, 'E`NW': 2, 'F@LuO': 3, 'F@T~o': 3, 'F?CWw': 3, 'FLr~o': 3, 'F@Kzw':
4, 'Fs\\zw': 5, 'FCXzw': 3, 'FJq~w': 4, 'F@`zo': 3, 'FBejW': 3, 'F?CXW':
2, 'F@V~o': 3, 'DNw': 3, 'F@hqw': 3, 'FDZJw': 3, 'Ejmw': 4, 'F?LVW': 2,
'F@@Lw': 2, 'F?\\sw': 3, 'E`Nw': 3, 'FK??W': 1, 'F_StW': 2, 'DN{': 3,
'F?Cjw': 2, 'F?Gyo': 2, 'F@LCG': 2, 'FS\\zw': 4, 'F_?~o': 3, 'F`\\tw':
4, 'F~~~w': 6, 'FBEmW': 3, 'E?\\o': 3, 'F?H[w': 2, 'EGNW': 2, 'F@L|w':
4, 'F?CaW': 2, 'E?\\w': 3, 'F`?}O': 2, 'FGSkg': 2, 'F`KqW': 3, 'F`N^w':
3, 'F?Lzw': 3, 'FJnNg': 4, 'EaMw': 2, 'Fbo|w': 3, 'FCX_w': 3, 'FLvvO':
4, 'F_?@w': 2, 'F???G': 1, 'F?LuW': 3, 'F^~~w': 5, 'F`v`w': 3, 'F@MZw':
3, 'F`Kzw': 4, 'FDpzw': 3, 'F_Cnw': 2, 'F?Lzo': 3, 'FDPlw': 2, 'A?': 1,
'F?T|o': 3, 'F??Nw': 2, 'F@^~w': 4, 'FB\\tW': 3, 'EKNG': 2, 'F@H[o': 3,
'E?Cw': 2, 'F@Oxw': 3, 'FBj~w': 3, 'EBXw': 3, 'F_D|w': 3, 'F??Ng': 2,
'F@H[w': 3, 'EENg': 3, 'FAM~w': 3, 'F?Kpw': 3, 'E@Tw': 2, 'E?Cg': 1,
'EC\\w': 3, 'A_': 1, 'F?NFw': 2, 'E?C_': 1, 'F@U}w': 3, 'F?LCG': 1,
'E@JW': 2, 'E?CW': 2, 'FAM~O': 3, 'F?Cxw': 3, 'FG?Wo': 2, 'E@T_': 2,
'FJ]}w': 4, 'FLh}w': 4, 'FGL[w': 3, 'F?Cxo': 3, 'FG?Ww': 2, 'F?GYw': 2,
'F?lrg': 3, 'F?Ca?': 1, 'F_D|o': 3};

def get_mu_from_dict(graph):
    """
    For a given graph, look it up in mu_dict for its mu.
    
    INPUT
    graph: a graph with at most 7 vertices
    
    OUTPUT
    The corresponding value of mu.
    """
    h=graph.canonical_label();
    h_name=h.graph6_string();
    return mu_dict[h_name];

## Forbidden minors for linklessly embeddable.
PetersenFamily=graphs.petersen_family();

## This paragraph comes from http://ask.sagemath.org/question/
## 8112/graph-minor-code-too-slow-in-certain-situations-sage-46/
def has_minor(G, H):
    try:
        m = G.minor(H)
        return True
    except ValueError: 
        return False


def find_mu(g):
    """
    Try to find mu for a given graph, by low-value tests, such 
    as planarity.
    
    INPUT
    g: a graph
    
    OUTPUT
    mu, if the exact value is determined;
    (low_bound,up_bound), otherwise.
    """
    n=g.order();
    low_bound,up_bound=0,n;
    min_deg=n-1;
    max_deg=0;
    ## Get min/max_deg
    for i in g.vertices():
        deg=g.degree(i);
        if deg<min_deg:
            min_deg=deg;
        if deg>max_deg:
            max_deg=deg; 
    ## Decrease up_bound
    if min_deg==n-1:
        return n-1;
    up_bound=n-2;     
    ## This up_bound does not apply for K2,
    ## but doesn't change the result.
    ## Increase low_bound         
    if n==1:
        return 0;
    if g.is_forest():
        if max_deg<=2:
            return 1;
        return 2;                
    if g.is_circular_planar():
        return 2;
    if g.is_planar():
        return 3;
    low_bound=4;
    for p in PetersenFamily:
        if has_minor(g,p):
            low_bound=5;
    if low_bound==4:
        return 4;
    ## No idea now.
    up_bound=min(up_bound,mu_upper(g));
    if low_bound==up_bound:
        return low_bound;
    return (low_bound,up_bound);
## Need has_minor function and PetersenFamily list.
## Minor algorithm works slow.

def no_twin(g):
    L=g.vertices();
    NBR=[g.neighbors(v) for v in L];
    n=len(L);
    again=True;
    for i in range(n-1):
        for j in range(i+1,n):
            Ni=NBR[i];
            Nj=NBR[j];
            if L[j] in Ni:
                Ni.remove(L[j]);
            if L[i] in Nj:
                Nj.remove(L[i]);              
            if Ni==Nj:
                again=False;
    return again;   
    
def mu_upper(g):
    n=g.order();
    e=g.size();
    rough_bdd=int(-0.5+sqrt(2*n+2*e+0.25));
    upper=n-1;
    if e==0:
        return min(n-1,1);
    if min(g.degree())==n-1:
        return n-1;
    else:
        upper=n-2; 
        ## This upper doesn't work for K2.
    h=g.complement();
    if not no_twin(h):
        return min(upper,rough_bdd);
    else:        
        if not h.is_circular_planar():
            upper=n-4;
        if not h.is_planar():
            upper=n-5;
    return min(upper,rough_bdd);
