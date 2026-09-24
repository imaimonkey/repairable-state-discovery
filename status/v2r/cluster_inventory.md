# V2R cluster inventory

2026-09-24T10:48:27.717969+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324405043200 available bytes; 81.90% used; 112489137 free inodes.

server1 `/home`: 324405043200 available bytes; 81.90% used; 112489137 free inodes.

server1 `/tmp`: 324405043200 available bytes; 81.90% used; 112489137 free inodes.

server1 `/var/tmp`: 324405043200 available bytes; 81.90% used; 112489137 free inodes.

server1 `/mnt/raid5`: 499773050880 available bytes; 97.71% used; 337695635 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57711661056 available bytes; 96.78% used; 110430419 free inodes.

server2 `/home`: 57711661056 available bytes; 96.78% used; 110430419 free inodes.

server2 `/tmp`: 57711661056 available bytes; 96.78% used; 110430419 free inodes.

server2 `/var/tmp`: 57711661056 available bytes; 96.78% used; 110430419 free inodes.

server2 `/mnt/raid5`: 512225886208 available bytes; 96.46% used; 445174661 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85797228544 available bytes; 95.21% used; 114198200 free inodes.

server3 `/home`: 85797228544 available bytes; 95.21% used; 114198200 free inodes.

server3 `/data`: 164105797632 available bytes; 97.73% used; 225817863 free inodes.

server3 `/tmp`: 85797228544 available bytes; 95.21% used; 114198200 free inodes.

server3 `/var/tmp`: 85797228544 available bytes; 95.21% used; 114198200 free inodes.
| server4 | True | ['6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735483392 available bytes; 94.10% used; 114348970 free inodes.

server4 `/home`: 105735483392 available bytes; 94.10% used; 114348970 free inodes.

server4 `/data`: 132799537152 available bytes; 98.16% used; 225258325 free inodes.

server4 `/tmp`: 105735483392 available bytes; 94.10% used; 114348970 free inodes.

server4 `/var/tmp`: 105735483392 available bytes; 94.10% used; 114348970 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
