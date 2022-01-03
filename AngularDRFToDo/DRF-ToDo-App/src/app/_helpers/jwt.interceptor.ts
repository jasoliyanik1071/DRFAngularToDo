import { Injectable } from '@angular/core';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor } from '@angular/common/http';
import { Observable } from 'rxjs';

import { environment } from '@environments/environment';
import { AccountService } from '@app/_services';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {
    constructor(private accountService: AccountService) { }

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        // add auth header with jwt if user is logged in and request is to the api url
        const user = this.accountService.userValue;
        var currentUserValue = user;

        if (currentUserValue != null){
            if ("data" in currentUserValue){
                var user_obj = currentUserValue.data;

                const isLoggedIn = user_obj && user_obj.jwt_token;
                const isApiUrl = request.url.startsWith(environment.apiUrl);
                if (isLoggedIn && isApiUrl) {
                    request = request.clone({
                        setHeaders: {
                            Authorization: `Bearer ${user_obj.jwt_token}`
                        }
                    });
                }
            }
        }else{

            const isLoggedIn = user && user.jwt_token;
            const isApiUrl = request.url.startsWith(environment.apiUrl);
            if (isLoggedIn && isApiUrl) {
                request = request.clone({
                    setHeaders: {
                        Authorization: `Bearer ${user.jwt_token}`
                    }
                });
            }

        }

        return next.handle(request);
    }
}