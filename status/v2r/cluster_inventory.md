# V2R cluster inventory

2026-09-25T02:29:55.947027+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318970441728 available bytes; 82.21% used; 112480498 free inodes.

server1 `/home`: 318970441728 available bytes; 82.21% used; 112480498 free inodes.

server1 `/tmp`: 318970441728 available bytes; 82.21% used; 112480498 free inodes.

server1 `/var/tmp`: 318970441728 available bytes; 82.21% used; 112480498 free inodes.

server1 `/mnt/raid5`: 416214286336 available bytes; 98.09% used; 337605954 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23016443904 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23016443904 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23016443904 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23016443904 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 483428765696 available bytes; 96.66% used; 445113870 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84351578112 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84351578112 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145603461120 available bytes; 97.99% used; 225811066 free inodes.

server3 `/tmp`: 84351578112 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84351578112 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['1', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105895837696 available bytes; 94.09% used; 114350973 free inodes.

server4 `/home`: 105895837696 available bytes; 94.09% used; 114350973 free inodes.

server4 `/data`: 20817362944 available bytes; 99.71% used; 224969199 free inodes.

server4 `/tmp`: 105895837696 available bytes; 94.09% used; 114350973 free inodes.

server4 `/var/tmp`: 105895837696 available bytes; 94.09% used; 114350973 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
