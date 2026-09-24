# V2R cluster inventory

2026-09-24T03:46:12.840853+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324741480448 available bytes; 81.88% used; 112493726 free inodes.

server1 `/home`: 324741480448 available bytes; 81.88% used; 112493726 free inodes.

server1 `/tmp`: 324741480448 available bytes; 81.88% used; 112493726 free inodes.

server1 `/var/tmp`: 324741480448 available bytes; 81.88% used; 112493726 free inodes.

server1 `/mnt/raid5`: 402122285056 available bytes; 98.16% used; 337724831 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40826134528 available bytes; 97.72% used; 110430980 free inodes.

server2 `/home`: 40826134528 available bytes; 97.72% used; 110430980 free inodes.

server2 `/tmp`: 40826134528 available bytes; 97.72% used; 110430980 free inodes.

server2 `/var/tmp`: 40826134528 available bytes; 97.72% used; 110430980 free inodes.

server2 `/mnt/raid5`: 526188056576 available bytes; 96.36% used; 445197317 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292366917632 available bytes; 83.68% used; 114198300 free inodes.

server3 `/home`: 292366917632 available bytes; 83.68% used; 114198300 free inodes.

server3 `/data`: 33877999616 available bytes; 99.53% used; 225842680 free inodes.

server3 `/tmp`: 292366917632 available bytes; 83.68% used; 114198300 free inodes.

server3 `/var/tmp`: 292366917632 available bytes; 83.68% used; 114198300 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105792749568 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105792749568 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 276811640832 available bytes; 96.17% used; 225384226 free inodes.

server4 `/tmp`: 105792749568 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105792749568 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
