import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {withStyles, Button, ListItem, ListItemSecondaryAction, Typography} from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import EditIcon from '@material-ui/icons/Edit';
import UpdateIcon from '@material-ui/icons/Update';
import  API  from '../api/API';
import List from '@material-ui/core/List';
import Checkbox from '@material-ui/core/Checkbox';
import ListeneintragLoeschen from "./dialogs/ListeneintragLoeschen";
import ListeneintragForm from "./dialogs/ListeneintragForm";
import ListeneintragBO from "../api/ListeneintragBO";

/** Rendert einen Listeneintrag in einer Einkaufsliste */

class ListenEintrag extends Component {

  constructor(props) {
    super(props);

    // Initialisiert ein leeres state
    this.state = {
      listeneintrag: this.props.listeneintrag,
      showForm: false
    };
  }

  eintragAbhaken = () => {
    let updatedListeneintrag = Object.assign(new ListeneintragBO(), this.state.listeneintrag);
    // Setzt die neuen Attribute aus dem Dialog
    updatedListeneintrag.setErledigt(true)
    API.getAPI().updateListeneintragAPI(updatedListeneintrag).then(listeneintrag=>{
      this.deleteListeneintragDialogClosed(listeneintrag);
    })
    };

  /** Behandelt das onClick Ereignis vom ListenEintragForm */
  deleteListeneintragButtonClicked = (event) => {
    event.stopPropagation();
    this.setState({
      showListeneintragDeleteDialog: true
    });
  }

  /** Behandelt das onClose Ereignis vom ListeneintragLoeschen Dialog */
  deleteListeneintragDialogClosed = (listeneintrag) => {
    // Wenn der Listeneintrag nicht gleich null ist, lösche ihn
    if (listeneintrag) {
      this.props.onListeneintragDeleted(listeneintrag);
    }
      this.setState({
      showListeneintragDeleteDialog: false
    });
  }

  /** Behandelt das onClick Ereignis vom ListenEintragForm zum updaten*/
  editButtonClicked=()=>{
    this.setState({
      showForm: true
    })
  }

  /** Behandelt das onClose Ereignis vom ArtikelForm */
  formClosed = (eintrag) => {
    // Listeneintrag ist nicht null und deshalb geändert.
    if (eintrag) {
      this.setState({
        listeneintrag: eintrag,
        showForm: false
      });
    } else {
      this.setState({
        showForm: false
      });
    }
  }

  /** Erstellt einen alert, der bei demdem zuletzt geänderten Listeneintrag erscheint. */
  latest() {
    alert("Dies ist der zuletzt geänderte Listeneintrag!");
  }

  /** Rendert die Komponente */
  render() {
    const { classes } = this.props;
    const { showListeneintragDeleteDialog, listeneintrag , showForm } = this.state;
    return (
      <div >
        <List  className={classes.Liste} >
        <ListItem>
          <Checkbox
              onChange={this.eintragAbhaken}
              inputProps={{ 'aria-label': 'primary checkbox' }}
          />
          <Typography color='textPrimary' className={classes.Artikel} >
            {listeneintrag.getArtikel_name()}
          </Typography>
          <Typography className={classes.Menge} color='textPrimary'>
            {listeneintrag.getMenge()?
               listeneintrag.getMenge() +"  "
            : null }
            {listeneintrag.getArtikel_einheit()}
          </Typography>
          <Typography className={classes.Ort} color='textPrimary'>
            {listeneintrag.getEinzelhaendler_name()}
          </Typography>
          <Typography className={classes.Benutzer} color='textPrimary'>
           {listeneintrag.getBenutzer_name()}
          </Typography>

          {listeneintrag.getZuletzt_geaendert()?
              <Button  color='secondary' size='small' startIcon={<UpdateIcon/>} onClick={this.latest}>
            </Button>
           : null
          }
          <ListItemSecondaryAction>
            <Button  color='secondary' size='small' startIcon={<EditIcon />} onClick={this.editButtonClicked}>
            </Button>
            <Button  color='secondary' size='small' startIcon={<DeleteIcon />} onClick={this.deleteListeneintragButtonClicked}>
            </Button>
          </ListItemSecondaryAction>
        </ListItem>
        </List>
        <ListeneintragForm  listeneintrag={listeneintrag} show={showForm} reload={this.props.reload} onClose={this.formClosed} einkaufsliste={this.props.einkaufsliste} />
        <ListeneintragLoeschen show={showListeneintragDeleteDialog}  listeneintrag={listeneintrag} onClose={this.deleteListeneintragDialogClosed} />
      </div>
    );
  }
}

/** Komponentenspezifisches Styling */
const styles = theme => ({
  root: {
    width: '100%'
  },

  buttonMargin: {
    marginRight: theme.spacing(2),
  },

  Artikel: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '25%',
    flexShrink: 0,
    align:'justify'
  },

  Liste:{
    listStyleType: false,
    variant: 'overline'
  },

  Menge: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '25%',
    flexShrink: 0,
    align:'justify'
  },

  Ort: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '25%',
    flexShrink: 0,
    align:'justify'
  },

  Benutzer: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '25%',
    flexShrink: 0,
    align:'justify'
  },
});

/** PropTypes */
ListenEintrag.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,

  listeneintrag: PropTypes.object.isRequired,
}

export default withStyles(styles)(ListenEintrag);
