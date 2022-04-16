import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-timeline',
  templateUrl: './timeline.component.html',
  styleUrls: ['./timeline.component.css']
})
export class TimelineComponent implements OnInit {
  token =sessionStorage.getItem('token')
  
token1 = "Token " + this.token;
httpOptions = {
  headers : new HttpHeaders ({
    'Content-type' : 'application/json',
    Authorization : String(this.token1)
    
  })}
  
  constructor(private http : HttpClient, private router: Router) {}
  first_name=''
  last_name=''
  ngOnInit(): void {
    let profile = this.http.get<any>(
      "http://localhost:8000/auth/v1/userprofile/" , this.httpOptions 
    ).subscribe(data =>{
      
      console.log(data.user)
      this.first_name = data.user['first_name']
      this.last_name = data.user['last_name']
      
      console.log(data['token'])
      sessionStorage.getItem('')
    
    });
    
  }


  gotoprofile():void{
    this.router.navigateByUrl('/userprofile');
    
    }

    
  gotofriendsuggestion():void{
      this.router.navigateByUrl('/friends');
      
      }

  gotofriends():void{
        this.router.navigateByUrl('/your_friends');
        
        }
      
    

  gototimeline1():void{
    this.router.navigateByUrl('/timeline1');
    
    }

  logout()
  {
    sessionStorage.removeItem('token')
    this.router.navigateByUrl('/');
  }

  tokenStatus()
  {
    if(this.token == null)
    {
      return false;
    }else{
      return true;
    }
  }
     
}
