import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';


import { environment } from '@environments/environment';
import { User } from '@app/_models';

import * as $ from "jquery";


@Injectable({ providedIn: 'root' })
export class AccountService {
    private userSubject: BehaviorSubject<User>;
    public user: Observable<User>;

    baseURL = "http://localhost:8000";
    httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})

    constructor(
        private router: Router,
        private http: HttpClient
    ) {
        if (JSON.parse(localStorage.getItem('user')) != null)
            this.userSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('user')).data);
        else
            this.userSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('user')));

        this.user = this.userSubject.asObservable();
    }


    public get userValue(): User {
        return this.userSubject.value;
    }

    login(email, password) {
        return this.http.post<User>(`${environment.apiUrl}/api/login`, { email, password })
            .pipe(map(user => {
                // store user details and jwt token in local storage to keep user logged in between page refreshes
                
                // Firstly remove all the stored item
                localStorage.removeItem('user');

                localStorage.setItem('user', JSON.stringify(user));
                this.userSubject.next(user);
                return user;
            }));
    }

    logout() {
        // remove user from local storage and set current user to null
        localStorage.removeItem('user');
        this.userSubject.next(null);
        this.router.navigate(['/account/login']);
    }

    register(user: User) {
        return this.http.post(`${environment.apiUrl}/api/register`, user);
    }

    getAll() {
        return this.http.get(this.baseURL + "/api/users/", {headers: this.httpHeaders})
    }    

    getById(id: string) {
        return this.http.get<User>(`${environment.apiUrl}/api/users/${id}`);
    }

    update(id, params) {
        return this.http.put(`${environment.apiUrl}/users/${id}`, params)
            .pipe(map(x => {
                // update stored user if the logged in user updated their own record
                if (id == this.userValue.id) {
                    // update local storage
                    const user = { ...this.userValue, ...params };
                    localStorage.setItem('user', JSON.stringify(user));

                    // publish updated user to subscribers
                    this.userSubject.next(user);
                }
                return x;
            }));
    }

    delete(id: string) {
        return this.http.delete(`${environment.apiUrl}/users/${id}`)
            .pipe(map(x => {
                // auto logout if the logged in user deleted their own record
                if (id == this.userValue.id) {
                    this.logout();
                }
                return x;
            }));
    }
}