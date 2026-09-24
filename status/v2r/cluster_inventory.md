# V2R cluster inventory

2026-09-24T09:04:24.149695+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324373200896 available bytes; 81.90% used; 112490105 free inodes.

server1 `/home`: 324373200896 available bytes; 81.90% used; 112490105 free inodes.

server1 `/tmp`: 324373200896 available bytes; 81.90% used; 112490105 free inodes.

server1 `/var/tmp`: 324373200896 available bytes; 81.90% used; 112490105 free inodes.

server1 `/mnt/raid5`: 483092123648 available bytes; 97.78% used; 337716443 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57786724352 available bytes; 96.78% used; 110430949 free inodes.

server2 `/home`: 57786724352 available bytes; 96.78% used; 110430949 free inodes.

server2 `/tmp`: 57786724352 available bytes; 96.78% used; 110430949 free inodes.

server2 `/var/tmp`: 57786724352 available bytes; 96.78% used; 110430949 free inodes.

server2 `/mnt/raid5`: 515390128128 available bytes; 96.44% used; 445178484 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85883244544 available bytes; 95.21% used; 114198832 free inodes.

server3 `/home`: 85883244544 available bytes; 95.21% used; 114198832 free inodes.

server3 `/data`: 167038484480 available bytes; 97.69% used; 225821770 free inodes.

server3 `/tmp`: 85883244544 available bytes; 95.21% used; 114198832 free inodes.

server3 `/var/tmp`: 85883244544 available bytes; 95.21% used; 114198832 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105759191040 available bytes; 94.10% used; 114349077 free inodes.

server4 `/home`: 105759191040 available bytes; 94.10% used; 114349077 free inodes.

server4 `/data`: 319629225984 available bytes; 95.58% used; 225273398 free inodes.

server4 `/tmp`: 105759191040 available bytes; 94.10% used; 114349077 free inodes.

server4 `/var/tmp`: 105759191040 available bytes; 94.10% used; 114349077 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
