import { Component,Inject } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
@Component({
    selector: 'view-dialog',
    templateUrl: './view.component.html',
    styleUrls: ['./view.component.css']
  })
  export class ViewDialog {
  
    constructor(
      public dialogRef: MatDialogRef<ViewDialog>,
      @Inject(MAT_DIALOG_DATA) public data: any) { }
  
    onNoClick(): void {
      this.dialogRef.close();
    }
  
  }
  