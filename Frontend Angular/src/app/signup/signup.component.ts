import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { FormControl, NgForm, Validators } from '@angular/forms';
 import {Route, Router} from '@angular/router';
import { catchError, throwError } from 'rxjs';
import { AuthService } from '../service/auth.service';




@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  RegisterView = {}

constructor(private router:Router, private httpClient: HttpClient) { 

}

ngOnInit(): void {
}

firstName = new FormControl('', [Validators.required])
lastName = new FormControl('', [Validators.required])
email = new FormControl('', [Validators.required])
password = new FormControl('', [Validators.required])

handleError(error: HttpErrorResponse){
  alert("You have already registered ! Try Login")
  return throwError(error)
  
}


Registration(registerForm: NgForm){
  

  let registerData = {
    first_name : registerForm.controls['firstName'].value,
    last_name : registerForm.controls['lastName'].value,
    email : registerForm.controls['email'].value,
    password : registerForm.controls['password'].value
  }

  console.log(registerData)

  console.log(registerForm.controls['firstName'].value)
  console.log(registerForm.controls['email'].value)


  let resp = this.httpClient.post<any>(
    "http://127.0.0.1:8000/auth/v1/register/",
  registerData).pipe(catchError(this.handleError))

  resp.subscribe(data=>{
    console.log(data)
    alert("Successfully Registred")
    this.router.navigateByUrl('/')
  })
}



// redirectToLogin(){
//   this.router.navigateByUrl('/');
// }

// conformRegister(){
//   this.router.navigateByUrl('');

// }

}

