import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { AuthService } from '../service/auth.service';


export interface FriendRequests {
  id:number,
  first_name:string,
  last_name:string,
  email:string,
  pic:string
}
@Component({
  selector: 'app-friends',
  templateUrl: './friends.component.html',
  styleUrls: ['./friends.component.css']
})



  
export class FriendsComponent implements OnInit {
fileToUpload: File | null = null;
friends : any
token =sessionStorage.getItem('token')
token1 = "Token " + this.token;


httpOptions = {
  headers : new HttpHeaders({
    'Content-type' : 'application/json',
    Authorization : String(this.token1)
    
  })} 
constructor(private http : HttpClient) { }

first_name=''
last_name=''  
friendRequestsList:any[] = []
freqdetails:FriendRequests[] =[]
user_dataset:any


  ngOnInit(): void 
  {
    //getfreqs/

    let getfresrequest = this.http.get<any>("http://127.0.0.1:8000/auth/v1/getfreqs/", this.httpOptions).subscribe
    ((data)=>{
      
      for(var i=0; i< data.length; i++)
      {
        
        this.friendRequestsList.push(data[i].from_user)
      }
      
    })
    //console.log(this.friendRequestsList)
    console.log(this.friendRequestsList[1])
    this.friendRequestsList.forEach(element => {
      console.log(element)
      this.http.get<any>("http://127.0.0.1:8000/auth/v1/userprofile/"+element+"/", this.httpOptions).subscribe
          ((data)=>{
              console.log ("dsdsd"+data)
              
          })
      
    });
   

    this.http.get<any>("http://127.0.0.1:8000/auth/v1/allusers/").subscribe
    ((data)=>{
      //console.log(data)
      this.friends = data
      //console.log()
    })


    


  }

  
 addFriendButton:boolean=true
  addFriend(event:any)
  {
    
   

    this.addFriendButton = false
    
    this.http.post<any>(
      "http://localhost:8000/auth/v1/sendfreq/" , {to_user : event,
      from_user : ''},this.httpOptions).subscribe(data =>{
      
      console.log(data)
      alert("friend added")
    
    })
    
  }

}
