import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-your-friends',
  templateUrl: './your-friends.component.html',
  styleUrls: ['./your-friends.component.css']
})
export class YourFriendsComponent implements OnInit {
token =sessionStorage.getItem('token')
token1 = "Token " + this.token;
httpOptions = {
  headers : new HttpHeaders ({
    'Content-type' : 'application/json',
    Authorization : String(this.token1)
    
  })}
  constructor(private http : HttpClient, private router: Router) {}
  friend_array:any[] = []
  friend_details:any[] = []
  ngOnInit(): void 
  {

    this.http.get<any>(
      "http://localhost:8000/auth/v1/userprofile/" , this.httpOptions 
    ).subscribe(data =>{
      
    //console.log(data.friends);
    this.friend_array = data.friends;
    //console.log(this.friend_array)
    for(var i=0;i<this.friend_array.length;i++){
      this.http.get<any>(
        "http://localhost:8000/auth/v1/userprofile/"+this.friend_array[i]+"/" , this.httpOptions 
      ).subscribe(data =>{
        
      //console.log(data);
      this.friend_details.push(data)
      });
    }
    });

    console.log(this.friend_details)
  }
  

}
