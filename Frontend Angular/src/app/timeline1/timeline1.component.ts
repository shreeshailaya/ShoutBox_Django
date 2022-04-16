import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-timeline1',
  templateUrl: './timeline1.component.html',
  styleUrls: ['./timeline1.component.css']
})
export class Timeline1Component implements OnInit {
  
  lists : any

//get the particular token for that user
token =sessionStorage.getItem('token')
token2 = "Token " + this.token;

//pass that token in headers
httpOptions = {
  headers : new HttpHeaders ({
    'Content-type' : 'application/json',
    Authorization : String(this.token2)
    
  })}

  toggle = true;
  status = 'Like';
  
  constructor(private http: HttpClient) { }

  


  ngOnInit(): void { //to get all shouts
    let getPost = this.http.get<any>("http://127.0.0.1:8000/auth/v2/getposts/", this.httpOptions)
    .subscribe((data)=>{
      console.log(data)
      this.lists = data
      console.log(data['first_name'])
    })
  }


  enableDisableRule(){
    this.toggle = !this.toggle;
    this.status = this.toggle ? 'Like' : 'Like'
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

  postData(){
    let getPost = this.http.post<any>("http://127.0.0.1:8000/auth/v2/postposts/", this.httpOptions)
    .subscribe((data)=>{
      console.log(data)
      this.lists = data
      console.log(data['first_name'])
    })

  }

}
