import { Component, OnInit, Inject } from '@angular/core';

import * as $ from "jquery";

import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

import { DjangoapiService } from './../shared/djangoapi.service';


@Component({
    selector: 'app-delete-todo-dialog',
    templateUrl: './delete-todo-dialog.component.html',
    // styleUrls: ['./delete-todo-dialog.component.css']
    styleUrls: ['./../todos/todos.component.scss'],
})

export class DeleteTodoDialogComponent implements OnInit {

    constructor(private djangoapi: DjangoapiService, public dialogRef: MatDialogRef<DeleteTodoDialogComponent>, @Inject(MAT_DIALOG_DATA) public todo: any) { }

    ngOnInit(): void {
    }

    close() {
        this.dialogRef.close();
    }

    deleteToDoConfirmation(todo: any) {

        this.djangoapi.deleteToDo(todo.id).subscribe(
            data => {
                console.log("ToDo deleted successfully!!!");
                window.alert("ToDo deleted successfully!!!");
                window.location.reload();
            },
            error => {
                console.log(error);
                window.alert("Something went wrong!!!");
                window.location.reload();
            }
        );
        this.dialogRef.close();
    }

}
