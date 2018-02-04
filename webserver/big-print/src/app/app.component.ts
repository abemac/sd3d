import { Component ,OnInit} from '@angular/core';
import { CreateDialog } from './create/create.component';
import { ViewDialog } from './view/view.component';
import { DiagnosticsDialog } from './diagnostics/diagnostics.component';
import { AboutDialog } from './about/about.component';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'BigPrint Control'
  
  constructor(public dialog: MatDialog) {}

  ngOnInit(){

  }

  openCreateDialog(){
    let dialogRef = this.dialog.open(CreateDialog, {
      width: '80%',
      height:'80%',
      data: { name: "this.name", animal: "this.animal" }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      //this.animal = result;
    });
  }
  
  openViewDialog(){
    let dialogRef = this.dialog.open(ViewDialog, {
      width: '80%',
      height:'80%',
      data: { name: "this.name", animal: "this.animal" }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      //this.animal = result;
    });
  }
  
  openDiagnosticsDialog(){
    let dialogRef = this.dialog.open(DiagnosticsDialog, {
      width: '80%',
      height:'80%',
      data: { name: "this.name", animal: "this.animal" }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      //this.animal = result;
    });
  }
  
  openAboutDialog(){
    let dialogRef = this.dialog.open(AboutDialog, {
      // width: '80%',
      // height:'80%',
      data: { name: "this.name", animal: "this.animal" }
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      //this.animal = result;
    });
  }
}
