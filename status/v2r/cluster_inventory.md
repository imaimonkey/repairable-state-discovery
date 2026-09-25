# V2R cluster inventory

2026-09-25T01:28:51.917746+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077629952 available bytes; 82.20% used; 112480757 free inodes.

server1 `/home`: 319077629952 available bytes; 82.20% used; 112480757 free inodes.

server1 `/tmp`: 319077629952 available bytes; 82.20% used; 112480757 free inodes.

server1 `/var/tmp`: 319077629952 available bytes; 82.20% used; 112480757 free inodes.

server1 `/mnt/raid5`: 416487436288 available bytes; 98.09% used; 337613097 free inodes.
| server2 | True | ['2', '6'] | [] |

server2 `/`: 23049289728 available bytes; 98.71% used; 110410774 free inodes.

server2 `/home`: 23049289728 available bytes; 98.71% used; 110410774 free inodes.

server2 `/tmp`: 23049289728 available bytes; 98.71% used; 110410774 free inodes.

server2 `/var/tmp`: 23049289728 available bytes; 98.71% used; 110410774 free inodes.

server2 `/mnt/raid5`: 491158405120 available bytes; 96.61% used; 445161446 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355497984 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84355497984 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 146706780160 available bytes; 97.97% used; 225812312 free inodes.

server3 `/tmp`: 84355497984 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84355497984 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778905088 available bytes; 94.10% used; 114348290 free inodes.

server4 `/home`: 105778905088 available bytes; 94.10% used; 114348290 free inodes.

server4 `/data`: 53319602176 available bytes; 99.26% used; 225030681 free inodes.

server4 `/tmp`: 105778905088 available bytes; 94.10% used; 114348290 free inodes.

server4 `/var/tmp`: 105778905088 available bytes; 94.10% used; 114348290 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
