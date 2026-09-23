# V2R cluster inventory

2026-09-23T18:57:01.937881+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41345122304 available bytes; 97.69% used; 110435446 free inodes.

server2 `/home`: 41345122304 available bytes; 97.69% used; 110435446 free inodes.

server2 `/tmp`: 41345122304 available bytes; 97.69% used; 110435446 free inodes.

server2 `/var/tmp`: 41345122304 available bytes; 97.69% used; 110435446 free inodes.

server2 `/mnt/raid5`: 544171814912 available bytes; 96.24% used; 445213792 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293701804032 available bytes; 83.61% used; 114244207 free inodes.

server3 `/home`: 293701804032 available bytes; 83.61% used; 114244207 free inodes.

server3 `/data`: 52815757312 available bytes; 99.27% used; 225846582 free inodes.

server3 `/tmp`: 293701804032 available bytes; 83.61% used; 114244207 free inodes.

server3 `/var/tmp`: 293701804032 available bytes; 83.61% used; 114244207 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111411777536 available bytes; 93.78% used; 114373045 free inodes.

server4 `/home`: 111411777536 available bytes; 93.78% used; 114373045 free inodes.

server4 `/data`: 15056896 available bytes; 100.00% used; 225458128 free inodes.

server4 `/tmp`: 111411777536 available bytes; 93.78% used; 114373045 free inodes.

server4 `/var/tmp`: 111411777536 available bytes; 93.78% used; 114373045 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
