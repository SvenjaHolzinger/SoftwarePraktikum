import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Typography,Tabs, Tab, Paper} from "@material-ui/core";
import {Link as RouterLink} from "react-router-dom"
import FastfoodIcon from "@material-ui/icons/Fastfood";
import ListAltIcon from '@material-ui/icons/ListAlt';
import PeopleIcon from "@material-ui/icons/People";
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import BarChartIcon from '@material-ui/icons/BarChart';
import ProfileDropDown from '../dialogs/ProfileDropDown';

/** Erstellt den Kopfbereich und die Navigation für die SharedShoppingList */

class Header extends Component {

  constructor(props) {
    super(props);

    // Init ein leeres state
    this.state = {
      tabindex: 0
    };
  }

  /** Behandelt das onChange Event von den Tabs */
  handleTabChange = (e, newIndex) => {
    // console.log(newValue)
    this.setState({
      tabindex: newIndex
    })
  };

  /** Rendert die Komponente */
  render() {
   const { user } = this.props;
    return (
        <Paper variant='outlined'>
        <ProfileDropDown user={user} />
        <Typography variant='h3' component='h1' align='center'>
         ShoppingList
        </Typography>
        <Typography variant='h4' component='h2' align='center'>
          Meine Einkäufe
        </Typography>
         {
          user ?
            <Tabs variant="scrollable" scrollButtons="on" indicatorColor='primary' textColor='primary' value={this.state.tabindex} onChange={this.handleTabChange} >
              <Tab icon ={<ListAltIcon/>} label='Einkaufslisten' component={RouterLink} to={`/alleEinkaufslisten`} style={{margin: "auto"}} />
              <Tab icon ={<FastfoodIcon/>} label='Artikel' component={RouterLink} to={`/artikel`} style={{margin: "auto"}} />
              <Tab icon ={<PeopleIcon/>} label='Anwenderverbund' component={RouterLink} to={`/anwenderverbund`} style={{margin: "auto"}} />
              <Tab icon ={<ShoppingCartIcon/>} label='Einzelhändler' component={RouterLink} to={`/einzelhaendler`} style={{margin: "auto"}} />
              <Tab icon ={<BarChartIcon/>} label='Statistik' href="http://localhost:3001/"  target="_blank" style={{margin: "auto"}} />
            </Tabs>                                                                                                                                 // bei href muss die URL hin, auf der die Statistik läuft
             : null
        }
        </Paper>
    )
  }
}

/** PropTypes */
Header.propTypes = {
  /** Der eingeloggte Firebase User */
  user: PropTypes.object,
}

export default Header;