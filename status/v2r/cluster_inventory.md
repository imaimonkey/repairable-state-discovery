# V2R cluster inventory

2026-09-25T09:02:51.057723+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837870592 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318837870592 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318837870592 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318837870592 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 364187082752 available bytes; 98.33% used; 337556982 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22830432256 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22830432256 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22830432256 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22830432256 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 332497453056 available bytes; 97.70% used; 445093170 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436480000 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84436480000 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142373883904 available bytes; 98.03% used; 225811115 free inodes.

server3 `/tmp`: 84436480000 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84436480000 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105633009664 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633009664 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243384086528 available bytes; 96.64% used; 224999360 free inodes.

server4 `/tmp`: 105633009664 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633009664 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
