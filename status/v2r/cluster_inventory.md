# V2R cluster inventory

2026-09-26T03:15:19.499438+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417707008 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318417707008 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318417707008 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318417707008 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331052261376 available bytes; 98.48% used; 337545890 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942679040 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22942679040 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22942679040 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22942679040 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 287658233856 available bytes; 98.01% used; 445052837 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84310781952 available bytes; 95.30% used; 114152358 free inodes.

server3 `/home`: 84310781952 available bytes; 95.30% used; 114152358 free inodes.

server3 `/data`: 125435502592 available bytes; 98.27% used; 225830867 free inodes.

server3 `/tmp`: 84310781952 available bytes; 95.30% used; 114152358 free inodes.

server3 `/var/tmp`: 84310781952 available bytes; 95.30% used; 114152358 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105922318336 available bytes; 94.09% used; 114347152 free inodes.

server4 `/home`: 105922318336 available bytes; 94.09% used; 114347152 free inodes.

server4 `/data`: 109006225408 available bytes; 98.49% used; 224914847 free inodes.

server4 `/tmp`: 105922318336 available bytes; 94.09% used; 114347152 free inodes.

server4 `/var/tmp`: 105922318336 available bytes; 94.09% used; 114347152 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
