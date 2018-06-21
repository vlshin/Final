from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm



class UserFormView(View):
    form_class= UserForm
    template_name='templates/registration.html'
    #process form data
    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    #process form data 
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #cleaned(normalized) data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
    #returns User objects if credentials are correct
        user =authenticate(username=username,password=password)
        if user is not None:
            
            if user.is_active:
               login(request,user)
               return redirect('templates/home.html')
        return render(request,self.template_name,{'form':form})
#------------------------------------------------------
class HomePage(TemplateView):
    template_name='home.html'
class LanguagesPage(TemplateView):
    template_name='languages.html'  
class LoginPage(TemplateView):
    template_name='login.html'
class LogOutPage(TemplateView):
    template_name='logged_out.html'
class RegistrationPage(TemplateView):
    template_name='registration.html'
    #------------------------------------------------------
class TestOrBegEng(TemplateView):
    template_name='TestOrBeginning/testorbegEng.html'
class TestOrBegFrc(TemplateView):
    template_name='TestOrBeginning/testorbegFrc.html'    
class TestOrBegSpa(TemplateView):
    template_name='TestOrBeginning/testorbegSpa.html'
    ##---------------------------------------------
class EngTestPage(TemplateView):
    template_name='testpages/EngTestPage.html'
class FrcTestPage(TemplateView):
    template_name='testpages/FrcTestPage.html'    
class SpaTestPage(TemplateView):
    template_name='testpages/SpaTestPage.html'
    ##---------------------------------------------
class EngTopicsPageBeg(TemplateView):
    template_name='topicspage/english/eng_topics_beg.html'
class FrcTopicsPageBeg(TemplateView):
    template_name='topicspage/french/frc_topics_beg.html'
class SpaTopicsPageBeg(TemplateView):
    template_name='topicspage/spanish/spa_topics_beg.html'
    ##---------------------------------------------
class EngTopicsPageInt(TemplateView):
    template_name='topicspage/english/eng_topics_int.html'
class FrcTopicsPageInt(TemplateView):
    template_name='topicspage/french/frc_topics_int.html'
class SpaTopicsPageInt(TemplateView):
    template_name='topicspage/spanish/spa_topics_int.html'
    ##---------------------------------------------
class EngTopicsPageAdv(TemplateView):
    template_name='topicspage/english/eng_topics_adv.html'
class SpaTopicsPageAdv(TemplateView):
    template_name='topicspage/spanish/spa_topics_adv.html'
class FrcTopicsPageAdv(TemplateView):
    template_name='topicspage/french/frc_topics_adv.html'
##----------------------------------------------------------
class EngAlphBeg(TemplateView):
    template_name='topics/beginner/english/eng_alphabet_beg.html'
class EngClothBeg(TemplateView):
    template_name='topics/beginner/english/eng_clothes_beg.html'
class EngNumBeg(TemplateView):
    template_name='topics/beginner/english/eng_numbers_beg.html'
class EngColorBeg(TemplateView):
    template_name='topics/beginner/english/eng_colors_beg.html'
class EngFruitBeg(TemplateView):
    template_name='topics/beginner/english/eng_fruits_beg.html'
##-----------------------------------------------------------------
class SpaAlphBeg(TemplateView):
    template_name='topics/beginner/spanish/spa_alphabet_beg.html'
class SpaClothBeg(TemplateView):
    template_name='topics/beginner/spanish/spa_clothes_beg.html'
class SpaNumBeg(TemplateView):
    template_name='topics/beginner/spanish/spa_numbers_beg.html'
class SpaColorBeg(TemplateView):
    template_name='topics/beginner/spanish/spa_colors_beg.html'
class SpaFruitBeg(TemplateView):
    template_name='topics/beginner/spanish/spa_fruits_beg.html'
##-------------------------------------------------------------------
class FrcAlphBeg(TemplateView):
    template_name='topics/beginner/french/frc_alphabet_beg.html'
class FrcClothBeg(TemplateView):
    template_name='topics/beginner/french/frc_clothes_beg.html'
class FrcNumBeg(TemplateView):
    template_name='topics/beginner/french/frc_numbers_beg.html'
class FrcColorBeg(TemplateView):
    template_name='topics/beginner/french/frc_colors_beg.html'
class FrcFruitBeg(TemplateView):
    template_name='topics/beginner/french/frc_fruits_beg.html'
    ##----------------------------------------------------------
class EngDial1Adv(TemplateView):
    template_name='topics/advanced/english/eng_dialog1_adv.html'
class EngDial2Adv(TemplateView):
    template_name='topics/advanced/english/eng_dialog2_adv.html'
class EngSongAdv(TemplateView):
    template_name='topics/advanced/english/eng_song_adv.html'
        ##----------------------------------------------------------
class FrcSong2Adv(TemplateView):
    template_name='topics/advanced/french/frc_song2_adv.html'
class FrcDial1Adv(TemplateView):
    template_name='topics/advanced/french/frc_dialog1_adv.html'
class FrcSong1Adv(TemplateView):
    template_name='topics/advanced/french/frc_song1_adv.html'
        ##----------------------------------------------------------
class SpaDial1Adv(TemplateView):
    template_name='topics/advanced/spanish/spa_dialog1_adv.html'
class SpaDial2Adv(TemplateView):
    template_name='topics/advanced/spanish/spa_dialog2_adv.html'
class SpaSongAdv(TemplateView):
    template_name='topics/advanced/spanish/spa_song_adv.html'
        ##----------------------------------------------------------
class EngPrInt(TemplateView):
    template_name='topics/intermediate/english/eng_present_int.html'
class EngPsInt(TemplateView):
    template_name='topics/intermediate/english/eng_past_int.html'
class EngFtInt(TemplateView):
    template_name='topics/intermediate/english/eng_future_int.html'
class EngThisInt(TemplateView):
    template_name='topics/intermediate/english/eng_this_int.html'
class EngInfinInt(TemplateView):
    template_name='topics/intermediate/english/eng_infin_int.html'
    ##------------------------------------------------------------
class FrcPrInt(TemplateView):
    template_name='topics/intermediate/french/frc_present_int.html'
class FrcPsInt(TemplateView):
    template_name='topics/intermediate/french/frc_past_int.html'
class FrcFtInt(TemplateView):
    template_name='topics/intermediate/french/frc_future_int.html'
class FrcThisInt(TemplateView):
    template_name='topics/intermediate/french/frc_this_int.html'
class FrcInfinInt(TemplateView):
    template_name='topics/intermediate/french/frc_infin_int.html'
    ##------------------------------------------------------------
class SpaPrInt(TemplateView):
    template_name='topics/intermediate/spanish/spa_present_int.html'
class SpaPsInt(TemplateView):
    template_name='topics/intermediate/spanish/spa_past_int.html'
class SpaFtInt(TemplateView):
    template_name='topics/intermediate/spanish/spa_future_int.html'
class SpaThisInt(TemplateView):
    template_name='topics/intermediate/spanish/spa_this_int.html'
class SpaInfinInt(TemplateView):
    template_name='topics/intermediate/spanish/spa_infin_int.html'
     ##------------------------------------------------------------
class QuizEngBeg(TemplateView):
    template_name='testoflevels/english/test_beginner.html'
class WrTEngInt(TemplateView):
    template_name='testoflevels/english/test_inter.html'
class LisTEngAdv1(TemplateView):
    template_name='testoflevels/english/test_advanced1.html'
class LisTEngAdv2(TemplateView):
    template_name='testoflevels/english/test_advanced2.html'
         ##------------------------------------------------------------
class QuizFrcBeg(TemplateView):
    template_name='testoflevels/french/test_beginner.html'
class WrTFrcInt(TemplateView):
    template_name='testoflevels/french/test_inter.html'
class LisTFrcAdv1(TemplateView):
    template_name='testoflevels/french/test_advanced1.html'
             ##------------------------------------------------------------
class QuizSpaBeg(TemplateView):
    template_name='testoflevels/spanish/test_beginner.html'
class WrTSpaInt(TemplateView):
    template_name='testoflevels/spanish/test_inter.html'
class LisTSpaAdv1(TemplateView):
    template_name='testoflevels/spanish/test_advanced1.html'
class LisTSpaAdv2(TemplateView):
    template_name='testoflevels/spanish/test_advanced2.html'
