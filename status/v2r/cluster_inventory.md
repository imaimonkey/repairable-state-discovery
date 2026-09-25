# V2R cluster inventory

2026-09-25T03:48:19.302216+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318937137152 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318937137152 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318937137152 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318937137152 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 415748341760 available bytes; 98.09% used; 337596748 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22973476864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22973476864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22973476864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22973476864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 464333053952 available bytes; 96.79% used; 445111134 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341379072 available bytes; 95.29% used; 114156064 free inodes.

server3 `/home`: 84341379072 available bytes; 95.29% used; 114156064 free inodes.

server3 `/data`: 144280244224 available bytes; 98.01% used; 225817087 free inodes.

server3 `/tmp`: 84341379072 available bytes; 95.29% used; 114156064 free inodes.

server3 `/var/tmp`: 84341379072 available bytes; 95.29% used; 114156064 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683312640 available bytes; 94.10% used; 114350901 free inodes.

server4 `/home`: 105683312640 available bytes; 94.10% used; 114350901 free inodes.

server4 `/data`: 38665703424 available bytes; 99.47% used; 224965204 free inodes.

server4 `/tmp`: 105683312640 available bytes; 94.10% used; 114350901 free inodes.

server4 `/var/tmp`: 105683312640 available bytes; 94.10% used; 114350901 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
