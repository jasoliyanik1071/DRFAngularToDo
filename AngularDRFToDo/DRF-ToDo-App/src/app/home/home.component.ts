import { Component } from '@angular/core';

import { User } from '@app/_models';
import { AccountService } from '@app/_services';

@Component({ templateUrl: 'home.component.html' })
export class HomeComponent {
    user: User;

    constructor(private accountService: AccountService) {
        // this.user = this.accountService.userValue;

        var currentUserValue = this.accountService.userValue;
        if (currentUserValue != null){
            if ("data" in currentUserValue){
                this.user = currentUserValue.data;
            }else{
                this.user = currentUserValue;
            }
        }else{
            this.user = null;
        }

    }
}