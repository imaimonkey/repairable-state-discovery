# V2R cluster inventory

2026-09-24T12:03:40.694580+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324269928448 available bytes; 81.91% used; 112488335 free inodes.

server1 `/home`: 324269928448 available bytes; 81.91% used; 112488335 free inodes.

server1 `/tmp`: 324269928448 available bytes; 81.91% used; 112488335 free inodes.

server1 `/var/tmp`: 324269928448 available bytes; 81.91% used; 112488335 free inodes.

server1 `/mnt/raid5`: 397163556864 available bytes; 98.18% used; 337685445 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57626198016 available bytes; 96.79% used; 110429666 free inodes.

server2 `/home`: 57626198016 available bytes; 96.79% used; 110429666 free inodes.

server2 `/tmp`: 57626198016 available bytes; 96.79% used; 110429666 free inodes.

server2 `/var/tmp`: 57626198016 available bytes; 96.79% used; 110429666 free inodes.

server2 `/mnt/raid5`: 509316141056 available bytes; 96.48% used; 445172682 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85747654656 available bytes; 95.21% used; 114198321 free inodes.

server3 `/home`: 85747654656 available bytes; 95.21% used; 114198321 free inodes.

server3 `/data`: 142914117632 available bytes; 98.02% used; 225815620 free inodes.

server3 `/tmp`: 85747654656 available bytes; 95.21% used; 114198321 free inodes.

server3 `/var/tmp`: 85747654656 available bytes; 95.21% used; 114198321 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105718583296 available bytes; 94.10% used; 114348826 free inodes.

server4 `/home`: 105718583296 available bytes; 94.10% used; 114348826 free inodes.

server4 `/data`: 90595352576 available bytes; 98.75% used; 225257329 free inodes.

server4 `/tmp`: 105718583296 available bytes; 94.10% used; 114348826 free inodes.

server4 `/var/tmp`: 105718583296 available bytes; 94.10% used; 114348826 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
