from django.urls import path,include

from . import views

urlpatterns = [
    path('home',views.HomePage.as_view(), name='home'),
    path('register',views.RegistrationPage.as_view(), name='register'),
    path('lang',views.LanguagesPage.as_view(), name='languages'),
    path('login',views.LoginPage.as_view(), name='login'),
    path('logout',views.LogOutPage.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace = 'social')),
    #-------------------------------------------------------------------
    path('testorbegEng',views.TestOrBegEng.as_view(),name='choice'),
    path('testorbegSpa',views.TestOrBegSpa.as_view(),name='choice'),
    path('testorbegFrc',views.TestOrBegFrc.as_view(),name='choice'),
    #--------------------------------------------------------
    path('engtest',views.EngTestPage.as_view(),name='test'),
    path('frctest',views.FrcTestPage.as_view(),name='test'),
    path('spatest',views.SpaTestPage.as_view(),name='test'),
    ##------------------------------------------------------------------------------------
    path('english/beginner/topics',views.EngTopicsPageBeg.as_view(), name='eng_topics_beg'),
    path('french/beginner/topics',views.FrcTopicsPageBeg.as_view(), name='frc_topics_beg'),
    path('spanish/beginner/topics',views.SpaTopicsPageBeg.as_view(), name='spa_topics_beg'),
    ##--------------------------------------------------------------------------------------
    path('english/int/topics',views.EngTopicsPageInt.as_view(), name='eng_topics_int'),
    path('french/int/topics',views.FrcTopicsPageInt.as_view(), name='frc_topics_int'),
    path('spanish/int/topics',views.SpaTopicsPageInt.as_view(), name='spa_topics_int'),
    ##------------------------------------------------------------------------------------
    path('english/adv/topics',views.EngTopicsPageAdv.as_view(), name='eng_topics_adv'),
    path('french/adv/topics',views.FrcTopicsPageAdv.as_view(), name='frc_topics_adv'),
    path('spanish/adv/topics',views.SpaTopicsPageAdv.as_view(), name='spa_topics_adv'),
    ##-------------------------------------------------------------------------------------
    path('english/beginner/alphabet-eng',views.EngAlphBeg.as_view(), name='eng_alph_beg'),
    path('english/beginner/clothes-eng',views.EngClothBeg.as_view(), name='eng_cloth_beg'),
    path('english/beginner/fruits-eng',views.EngFruitBeg.as_view(), name='eng_fruit_beg'),
    path('english/beginner/numbers-eng',views.EngNumBeg.as_view(), name='eng_num_beg'),
    path('english/beginner/colors-eng',views.EngColorBeg.as_view(), name='eng_color_beg'),
    path('english/beginner/testbeg-eng',views.QuizEngBeg.as_view(), name='eng_test_beg'),
    ##-----------------------------------------------------------------------------------
    path('spanish/beginner/alphabet-spa',views.SpaAlphBeg.as_view(), name='spa_alph_beg'),
    path('spanish/beginner/clothes-spa',views.SpaClothBeg.as_view(), name='spa_cloth_beg'),
    path('spanish/beginner/fruits-spa',views.SpaFruitBeg.as_view(), name='spa_fruit_beg'),
    path('spanish/beginner/numbers-spa',views.SpaNumBeg.as_view(), name='spa_num_beg'),
    path('spanish/beginner/colors-spa',views.SpaColorBeg.as_view(), name='spa_color_beg'),
    path('spanish/beginner/testbeg-spa',views.QuizSpaBeg.as_view(), name='spa_test_beg'),
    ##----------------------------------------------------------------------------------------
    path('french/beginner/alphabet-frc',views.FrcAlphBeg.as_view(), name='frc_alph_beg'),
    path('french/beginner/clothes-frc',views.FrcClothBeg.as_view(), name='frc_cloth_beg'),
    path('french/beginner/fruits-frc',views.FrcFruitBeg.as_view(), name='frc_fruit_beg'),
    path('french/beginner/numbers-frc',views.FrcNumBeg.as_view(), name='frc_num_beg'),
    path('french/beginner/colors-frc',views.FrcColorBeg.as_view(), name='frc_color_beg'),
    path('french/beginner/testbeg-frc',views.QuizFrcBeg.as_view(), name='frc_test_beg'),
    ##-------------------------------------------------------------------------------------
    path('english/adv/dial1-eng',views.EngDial1Adv.as_view(), name='eng_dialog1_adv'),
    path('english/adv/dial2-eng',views.EngDial2Adv.as_view(), name='eng_dialog2_adv'),
    path('english/adv/song-eng',views.EngSongAdv.as_view(), name='eng_song_adv'),
    path('english/adv/listening1-eng',views.LisTEngAdv1.as_view(), name='eng_test1_adv'),
    path('english/adv/listening2-eng',views.LisTEngAdv2.as_view(), name='eng_test2_adv'),
    ##-------------------------------------------------------------------------------------
    path('spanish/adv/dial1-spa',views.SpaDial1Adv.as_view(), name='spa_dialog1_adv'),
    path('spanish/adv/dial2-spa',views.SpaDial2Adv.as_view(), name='spa_dialog2_adv'),
    path('spanish/adv/song-spa',views.SpaSongAdv.as_view(), name='spa_song_adv'),
    path('spanish/adv/listening1-spa',views.LisTSpaAdv1.as_view(), name='spa_test1_adv'),
    path('spanish/adv/listening2-spa',views.LisTSpaAdv2.as_view(), name='spa_test1_adv'),
    ##-------------------------------------------------------------------------------------
    path('french/adv/song2-frc',views.FrcSong2Adv.as_view(), name='frc_song2_adv'),
    path('french/adv/dial1-frc',views.FrcDial1Adv.as_view(), name='frc_dialog1_adv'),
    path('french/adv/song1-frc',views.FrcSong1Adv.as_view(), name='frc_song1_adv'),
    path('french/adv/listening1-frc',views.LisTFrcAdv1.as_view(), name='frc_test1_adv'),
        ##-------------------------------------------------------------------------------------
    path('english/int/present-eng',views.EngPrInt.as_view(), name='eng_present_int'),
    path('english/int/past-eng',views.EngPsInt.as_view(), name='eng_past_int'),
    path('english/int/future-eng',views.EngFtInt.as_view(), name='eng_future_int'),
    path('english/int/this-eng',views.EngThisInt.as_view(), name='eng_this_int'),
    path('english/int/infin-eng',views.EngInfinInt.as_view(), name='eng_infin_int'),
    path('english/int/writing-eng',views.WrTEngInt.as_view(), name='eng_test_int'),
    ##-------------------------------------------------------------------------------------
    path('spanish/int/present-spa',views.SpaPrInt.as_view(), name='spa_present_int'),
    path('spanish/int/past-spa',views.SpaPsInt.as_view(), name='spa_past_int'),
    path('spanish/int/future-spa',views.SpaFtInt.as_view(), name='spa_future_int'),
    path('spanish/int/this-spa',views.SpaThisInt.as_view(), name='spa_this_int'),
    path('spanish/int/infin-spa',views.SpaInfinInt.as_view(), name='spa_infin_int'),
    path('spanish/int/writing-spa',views.WrTSpaInt.as_view(), name='spa_test_int'),
    ##-------------------------------------------------------------------------------------
    path('french/int/present-frc',views.FrcPrInt.as_view(), name='frc_present_int'),
    path('french/int/past-frc',views.FrcPsInt.as_view(), name='frc_past_int'),
    path('french/int/future-frc',views.FrcFtInt.as_view(), name='frc_future_int'),
    path('french/int/this-frc',views.FrcThisInt.as_view(), name='frc_this_int'),
    path('french/int/infin-frc',views.FrcInfinInt.as_view(), name='frc_infin_int'),
    path('french/int/writing-frc',views.WrTFrcInt.as_view(), name='frc_test_int'),
]   ##-------------------------------------------------------------------------------------
    