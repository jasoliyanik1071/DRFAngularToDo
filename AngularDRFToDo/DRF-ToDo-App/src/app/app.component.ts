import { Component } from '@angular/core';

import { DjangoapiService } from './shared/djangoapi.service';

import { AccountService } from './_services';
import { User } from './_models';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';

import { FormControl, FormGroup } from '@angular/forms';


@Component({
    selector: 'app',
    templateUrl: './app.component.html',
    styleUrls: ['./todos/todos.component.scss'],

    providers: [DjangoapiService]
})
export class AppComponent {
    title = 'DRF-ToDo-App';
    baseURL = "http://localhost:8000";
    httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})

    dateRange = new FormGroup({
        start_date: new FormControl(),
        end_date: new FormControl()
    });

    user: User;
    constructor(private accountService: AccountService, private http: HttpClient) {
        this.accountService.user.subscribe(x => this.user = x);
    }

    logout() {
        this.accountService.logout();
    }
}

