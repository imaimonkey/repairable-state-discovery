# V2R cluster inventory

2026-09-25T03:10:24.098064+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318940868608 available bytes; 82.21% used; 112480385 free inodes.

server1 `/home`: 318940868608 available bytes; 82.21% used; 112480385 free inodes.

server1 `/tmp`: 318940868608 available bytes; 82.21% used; 112480385 free inodes.

server1 `/var/tmp`: 318940868608 available bytes; 82.21% used; 112480385 free inodes.

server1 `/mnt/raid5`: 416123125760 available bytes; 98.09% used; 337601224 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22990970880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22990970880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22990970880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22990970880 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 465799389184 available bytes; 96.78% used; 445112645 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84344664064 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84344664064 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 144854601728 available bytes; 98.00% used; 225810282 free inodes.

server3 `/tmp`: 84344664064 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84344664064 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692925952 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692925952 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 50245902336 available bytes; 99.31% used; 224967355 free inodes.

server4 `/tmp`: 105692925952 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692925952 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
