import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { TodosComponent } from './todos/todos.component';

import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, NgForm } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { TodoItemComponent } from './todo-item/todo-item.component';
import { EditTodoDialogComponent } from './edit-todo-dialog/edit-todo-dialog.component';
import { DeleteTodoDialogComponent } from './delete-todo-dialog/delete-todo-dialog.component';


import { ReactiveFormsModule } from '@angular/forms';

// used to create fake backend
import { fakeBackendProvider } from './_helpers';

import { JwtInterceptor, ErrorInterceptor } from './_helpers';
import { AlertComponent } from './_components';
import { HomeComponent } from './home';


import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatNativeDateModule } from '@angular/material/core';


@NgModule({
    declarations: [
        AppComponent,
        TodosComponent,
        TodoItemComponent,
        EditTodoDialogComponent,
        DeleteTodoDialogComponent,
        AlertComponent,
        HomeComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        HttpClientModule,
        MatDialogModule,
        FormsModule,
        ReactiveFormsModule,

        MatDatepickerModule,
        MatFormFieldModule,
        MatNativeDateModule
    ],
    exports:[FormsModule],
    providers: [
        { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
        { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

        // provider used to create fake backend
        fakeBackendProvider
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }

