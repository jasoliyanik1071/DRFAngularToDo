import { Injectable } from '@angular/core';

import { ToDo } from './todo.model';


import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { TodosComponent } from './../todos/todos.component';

import { Http, Headers, Response } from '@angular/http';



@Injectable({
  providedIn: 'root'
})
export class DjangoapiService {

    alltodos: TodosComponent[] = [];
    baseURL = "http://127.0.0.1:8000";
    httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});

    constructor(private http: HttpClient) { }

    updateRequestHeader(jwt_token){
        var local_storage_data = localStorage.getItem("user");
        if (local_storage_data){
            var parse_local_storage_data = JSON.parse(local_storage_data);
            if ("data" in parse_local_storage_data){
                var jwt_token = parse_local_storage_data.data.jwt_token;
            }
        } 

        var reqHeader = new HttpHeaders({ 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + jwt_token
        });

        return reqHeader;
    }

    getAllToDosfromDjango(): Observable<any>{
        var jwt_token = "Bearer fake-jwt-token";
        var reqHeader = this.updateRequestHeader(jwt_token);
        return this.http.get(this.baseURL + "/todoapp/api/todos/", {headers: reqHeader})
    }

    getSelectedToDo(id:any): Observable<any>{
        var jwt_token = "Bearer fake-jwt-token";
        var reqHeader = this.updateRequestHeader(jwt_token);
        return this.http.get(this.baseURL + "/todoapp/api/todos/" + id + "/", {headers: reqHeader})
    }

    toggleToDoStatusCompleted(todo:any): Observable<any>{
        var jwt_token = "Bearer fake-jwt-token";
        var reqHeader = this.updateRequestHeader(jwt_token);

        var params = {
            todo_status: false
        }
        if (!todo.todo_status){
            params = {
                todo_status: true
            }
        }
        return this.http.put(this.baseURL + "/todoapp/api/todos/" + todo.id + "/", params, {headers: reqHeader})
    }

    updateSelectedToDo(updated_params:any): Observable<any>{
        var jwt_token = "Bearer fake-jwt-token";
        var reqHeader = this.updateRequestHeader(jwt_token);
        return this.http.put(this.baseURL + "/todoapp/api/todos/" + updated_params.id + "/", updated_params, {headers: reqHeader})
    }

    createToDo(todo_params:any): Observable<any>{
        var jwt_token = "Bearer fake-jwt-token";
        var reqHeader = this.updateRequestHeader(jwt_token);
        return this.http.post(this.baseURL + "/todoapp/api/todos/", todo_params, {headers: reqHeader})
    }

    deleteToDo(id:any): Observable<any>{
        var jwt_token = "Bearer fake-jwt-token";
        var reqHeader = this.updateRequestHeader(jwt_token);
        return this.http.delete(this.baseURL + "/todoapp/api/todos/" + id + "/", {headers: reqHeader})
    }
}
