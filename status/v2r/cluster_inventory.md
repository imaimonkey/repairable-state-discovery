# V2R cluster inventory

2026-09-24T11:21:19.826500+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324355887104 available bytes; 81.91% used; 112488904 free inodes.

server1 `/home`: 324355887104 available bytes; 81.91% used; 112488904 free inodes.

server1 `/tmp`: 324355887104 available bytes; 81.91% used; 112488904 free inodes.

server1 `/var/tmp`: 324355887104 available bytes; 81.91% used; 112488904 free inodes.

server1 `/mnt/raid5`: 457455415296 available bytes; 97.90% used; 337690332 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57673203712 available bytes; 96.78% used; 110430088 free inodes.

server2 `/home`: 57673203712 available bytes; 96.78% used; 110430088 free inodes.

server2 `/tmp`: 57673203712 available bytes; 96.78% used; 110430088 free inodes.

server2 `/var/tmp`: 57673203712 available bytes; 96.78% used; 110430088 free inodes.

server2 `/mnt/raid5`: 510910722048 available bytes; 96.47% used; 445173733 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85760700416 available bytes; 95.21% used; 114197382 free inodes.

server3 `/home`: 85760700416 available bytes; 95.21% used; 114197382 free inodes.

server3 `/data`: 163861446656 available bytes; 97.74% used; 225816816 free inodes.

server3 `/tmp`: 85760700416 available bytes; 95.21% used; 114197382 free inodes.

server3 `/var/tmp`: 85760700416 available bytes; 95.21% used; 114197382 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105731170304 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105731170304 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115646267392 available bytes; 98.40% used; 225258098 free inodes.

server4 `/tmp`: 105731170304 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105731170304 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
