import { Component,Inject } from '@angular/core';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
@Component({
    selector: 'about-dialog',
    templateUrl: './about.component.html',
    styleUrls: ['./about.component.css']
  })
  export class AboutDialog {
  
    constructor(
      public dialogRef: MatDialogRef<AboutDialog>,
      @Inject(MAT_DIALOG_DATA) public data: any) { }
  
    onNoClick(): void {
      this.dialogRef.close();
    }
  
  }
  