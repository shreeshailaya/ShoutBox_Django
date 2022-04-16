import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './signup/signup.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { MainComponent } from './main/main.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { TimelineComponent } from './timeline/timeline.component';
import { FriendsComponent } from './friends/friends.component';
import { Timeline1Component } from './timeline1/timeline1.component';
import { AuthService } from './service/auth.service';
import { YourFriendsComponent } from './your-friends/your-friends.component';


@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    ProfileComponent,
    MainComponent,
    TimelineComponent,
    FriendsComponent,
    Timeline1Component,
    YourFriendsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
