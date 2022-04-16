import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { catchError, throwError } from 'rxjs';
import { Route, Router } from '@angular/router';

export interface LoginUserData
{
  username:string;
  password:string;
  token:string
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor( private httpClient: HttpClient,private router:Router) { }

  ngOnInit(): void {
  }
  handleError(error: HttpErrorResponse) {
      alert("username or password is invalid")
      return throwError(error);
  }

  loginHandler( loginForm : NgForm)
  {
    let userData = {
      username : loginForm.controls['email'].value,
      password : loginForm.controls['password'].value
  
    }
    console.log(userData)

  

    let resp = this.httpClient.post<LoginUserData>(
      "http://localhost:8000/auth/v1/login/",userData).pipe(catchError(this.handleError)).subscribe(data =>{
        console.log(data['token'])
        sessionStorage.setItem('token', data['token']); 
        //console.log("session tkn"+sessionStorage.getItem('token'))
        

      })
      console.log('nav')
      if(sessionStorage.getItem('token')){
        this.router.navigateByUrl('/userprofile');
      }

  }

}
