import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, ListItem, ListItemSecondaryAction, Link, Typography } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import SwapHoriz from '@material-ui/icons/SwapHoriz';
import { Link as RouterLink } from 'react-router-dom';
import { API } from '../api';
import List from '@material-ui/core/List';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';


/**
 * Renders a AccountBO object within a ListEntry and provides a delete button to delete it. Links accounts
 * to a list of transactions. This is done by routing the link to /transactions and passing the CustomerBO and
 * the AccountBO as props to the AccountList component. It also shows a MoneyTransferDialog to transfer money.
 *
 * @see See Material-UIs [Lists](https://material-ui.com/components/lists/)
 * @see See Material-UIs [ListItem](https://material-ui.com/api/list-item/)
 * @see See Material-UIs [Link](https://material-ui.com/components/links/)
 * @see See Material-UIs React Router integration [Composition](https://material-ui.com/guides/composition/#link)
 * @see See React Router [ReactRouter](https://reacttraining.com/react-router/web/guides/quick-start)
 * @see See React Router [Link](https://reacttraining.com/react-router/web/api/Link)
 *
 * @see See [MoneyTransferDialog](#moneytransferdialog)
 * @see See [TransactionList](#transactionlist)
 *
 * @author [Christoph Kunz](https://github.com/christophkunz)
 */
class ListenEintrag extends Component {

  constructor(props) {
    super(props);

    // Init an empty state
    this.state = {
      balance: '',
      loadingInProgress: false,
      deletingInProgress: false,
      loadingError: null,
      deletingError: null,
      showMoneyTransferDialog: false,
      checked:false

    };
  }


handleCheck =(event)=>{
    this.setState({
      checked: event.target.checked
        }

    )

}



  /** Renders the component */
  render() {
    const { classes, customer, account } = this.props;
    const { loadingInProgress, deletingInProgress, loadingError, deletingError, balance, showMoneyTransferDialog,checked } = this.state;

    return (
      <div >
        <List  className={classes.Liste} >
        <ListItem >
          <Checkbox
              checked={checked}
              onChange={this.handleCheck}
              inputProps={{ 'aria-label': 'primary checkbox' }}
          />

          <Typography color='textPrimary' className={classes.accountEntry} >
            Artikel

          </Typography>
          <Typography className={classes.Menge} color='textPrimary'>
            Menge
          </Typography>

          <Typography className={classes.Ort} color='textPrimary'>
            Einkaufsort
          </Typography>

          <ListItemSecondaryAction>

            <Button color='secondary' size='small' startIcon={<DeleteIcon />} onClick={this.deleteAccount}>
              Delete
            </Button>
          </ListItemSecondaryAction>
        </ListItem>
        </List>

      </div>
    );
  }
}

/** Component specific styles */
const styles = theme => ({
  root: {
    width: '100%'
  },
  buttonMargin: {
    marginRight: theme.spacing(2),
  },
    accountEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,

  },
    Liste:{
    listStyleType: false,
    variant: 'overline'
    },

    Menge: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
    },

    Ort: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '23.33%',
    flexShrink: 0,

    },


});

/** PropTypes */
ListenEintrag.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** The CustomerBO of this AccountListEntry */
  customer: PropTypes.object.isRequired,
  /** The AccountBO to be rendered */
  account: PropTypes.object.isRequired,
  /**
   * Event Handler function which is called after a sucessfull delete of this account.
   *
   * Signature: onAccountDeleted(AccountBO account);
   */
  onAccountDeleted: PropTypes.func.isRequired,
  /** If true, balance is (re)loaded */
  show: PropTypes.bool.isRequired
}

export default withStyles(styles)(ListenEintrag);
