import React from 'react';
import "./sidebar.css"

const SidebarItem = (props) => {
	const active = props.active ? 'active' : '';

	return (
		<div className="sidebar__item">
			<div className={`sidebar__item-inner ${active}`}>
				<i className={props.icon}/>
				<span>{props.title}</span>
			</div>
		</div>
	);
};

export default SidebarItem;