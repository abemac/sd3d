import { Component,Inject } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
@Component({
    selector: 'create-dialog',
    templateUrl: './create.component.html',
    styleUrls: ['./create.component.css']
  })
  export class CreateDialog {
  
    constructor(
      public dialogRef: MatDialogRef<CreateDialog>,
      @Inject(MAT_DIALOG_DATA) public data: any) { }
  
    onNoClick(): void {
      this.dialogRef.close();
    }
  
  }
  