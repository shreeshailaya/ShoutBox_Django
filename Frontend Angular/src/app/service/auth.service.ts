import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  //private registerUrl = "http://localhost:8000/auth/v1/register/"


  token =sessionStorage.getItem('token')
  token1 = "Token " + this.token;

  constructor(private http : HttpClient) { }

  httpOptions = {
    headers : new HttpHeaders ({
      'Content-type' : 'application/json',
      Authorization : String(this.token1)
      
    })
    

  }
  // for  user profile
  users()
  {
    return this.http.get("http://localhost:8000/auth/v1/userprofile/", this.httpOptions); 
  }

  //for friendList

  friend()
  {
    return this.http.get("http://127.0.0.1:8000/auth/v1/friends/");
  }
}
