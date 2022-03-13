import React from 'react';
import sidebar_items from '../../assets/JsonData/sidebar_routes.json'
import logo from '../../assets/images/logo.png'
import {Link, useLocation} from "react-router-dom"
import "./sidebar.css"

const SidebarItem = props => {
	const active = props.active ? 'active' : '';
	return (
		<div className="sidebar__item">
				<div className={`sidebar__item-inner ${active}`}>
					<i className={props.icon}/>
					<span>{props.title}</span>
				</div>
		</div>
	)
}

const Sidebar = () => {
	const location = useLocation();
	const activeItem = sidebar_items.findIndex(item => item.route === location.pathname)
	return (
		<div className="sidebar">
			<div className="sidebar__logo">
				<img src={logo} alt="logo"/>
			</div>
			{
				sidebar_items.map((item, index) => (
					<Link to={item.route} key={index}>
						<SidebarItem
							title={item.display_name}
							icon={item.icon}
							active={index === activeItem}
						/>
					</Link>
				))
			}
		</div>
	);
};

export default Sidebar;