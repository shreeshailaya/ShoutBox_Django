import { Component, OnInit, Input } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { catchError, Observable, of, throwError } from 'rxjs';
import { Router } from '@angular/router';
import { AuthService } from '../service/auth.service';

export interface profileUserData 
{
  first_name: string;
  last_name: string;
  email: string;
  bio: string;
  mobie: string;
  dob: string;
  city: string;
  work_at: string;
  gender: string;
  token : string
}

 

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {


  //users: any
token =sessionStorage.getItem('token')
token1 = "Token " + this.token;
httpOptions = {
  headers : new HttpHeaders ({
    'Content-type' : 'application/json',
    Authorization : String(this.token1)
    
  })}
 
  tokenStatus()	 
		  {
		    if(this.token == null)
		    {
		      return false;
		    }else{
		      return true;
		    }
		  }



  constructor(private http : HttpClient, private router: Router) {}


  private handleAuthError(err: HttpErrorResponse): Observable<any> {
    //handle your auth error or rethrow
    if (err.status === 401 || err.status === 403) {
        
        
      
      return of(err.message); 
    }
    return throwError(err);
}

first_name=''
last_name=''
email=''

  ngOnInit(): void {

    console.log(HttpHeaders)
    let profile = this.http.get<any>(
      "http://localhost:8000/auth/v1/userprofile/" , this.httpOptions 
    ).subscribe(data =>{
      
      console.log(data.user)
      this.first_name = data.user['first_name']
      this.last_name = data.user['last_name']
      this.email = data.user['email']
      console.log(data['token'])
      //sessionStorage.getItem('')
    
    })
    
  }

  

  
    
    

  

}


// let profile = this.http.get<profileUserData>(
//   "http://localhost:8000/auth/v1/userprofile/" 
// ).subscribe(data =>{
//   console.log(data['token'])
//   sessionStorage.getItem('')

// })

// }

// const httpOptions = {
//   headers: new HttpHeaders({
//     // 'Authorization': 'json/Application',
//   sessionStorage.getItem('token')
//   })
// };

// return this.http.get('http://localhost:8000/auth/v1/userprofile/', httpOptions);

