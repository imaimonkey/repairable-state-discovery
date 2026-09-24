# V2R cluster inventory

2026-09-24T12:00:33.582708+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324276269056 available bytes; 81.91% used; 112488365 free inodes.

server1 `/home`: 324276269056 available bytes; 81.91% used; 112488365 free inodes.

server1 `/tmp`: 324276269056 available bytes; 81.91% used; 112488365 free inodes.

server1 `/var/tmp`: 324276269056 available bytes; 81.91% used; 112488365 free inodes.

server1 `/mnt/raid5`: 408806981632 available bytes; 98.12% used; 337685849 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57631064064 available bytes; 96.78% used; 110429696 free inodes.

server2 `/home`: 57631064064 available bytes; 96.78% used; 110429696 free inodes.

server2 `/tmp`: 57631064064 available bytes; 96.78% used; 110429696 free inodes.

server2 `/var/tmp`: 57631064064 available bytes; 96.78% used; 110429696 free inodes.

server2 `/mnt/raid5`: 509416841216 available bytes; 96.48% used; 445172827 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85748649984 available bytes; 95.21% used; 114198301 free inodes.

server3 `/home`: 85748649984 available bytes; 95.21% used; 114198301 free inodes.

server3 `/data`: 163584462848 available bytes; 97.74% used; 225815678 free inodes.

server3 `/tmp`: 85748649984 available bytes; 95.21% used; 114198301 free inodes.

server3 `/var/tmp`: 85748649984 available bytes; 95.21% used; 114198301 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105718689792 available bytes; 94.10% used; 114348826 free inodes.

server4 `/home`: 105718689792 available bytes; 94.10% used; 114348826 free inodes.

server4 `/data`: 112012066816 available bytes; 98.45% used; 225257779 free inodes.

server4 `/tmp`: 105718689792 available bytes; 94.10% used; 114348826 free inodes.

server4 `/var/tmp`: 105718689792 available bytes; 94.10% used; 114348826 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
