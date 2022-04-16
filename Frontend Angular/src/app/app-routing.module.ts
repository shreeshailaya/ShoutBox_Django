import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FriendsComponent } from './friends/friends.component';
// import { type } from 'os';
import { LoginComponent } from './login/login.component';
import { MainComponent } from './main/main.component';
import { ProfileComponent } from './profile/profile.component';
import { SignupComponent } from './signup/signup.component';
import { TimelineComponent } from './timeline/timeline.component';
import { Timeline1Component } from './timeline1/timeline1.component';
import { YourFriendsComponent } from './your-friends/your-friends.component';

const routes: Routes = [
   {path:'', component:MainComponent},
   {path:'signup' , component:SignupComponent}, //login page signup button
  //  {path:'login' , component:LoginComponent},
  // {component: SignupComponent,path:'signup'}
   {path:'userprofile',component:ProfileComponent},
  //  {path:'sign_up',redirectTo:" ",pathMatch:'full'},
   {path:'timeline',component:TimelineComponent},
   {path:'friends',component:FriendsComponent},
   {path:'timeline1',component:Timeline1Component},
   {path:'your_friends',component:YourFriendsComponent}
   



  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


