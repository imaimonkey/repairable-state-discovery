# V2R cluster inventory

2026-09-25T15:38:12.011523+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318691893248 available bytes; 82.22% used; 112476531 free inodes.

server1 `/home`: 318691893248 available bytes; 82.22% used; 112476531 free inodes.

server1 `/tmp`: 318691893248 available bytes; 82.22% used; 112476531 free inodes.

server1 `/var/tmp`: 318691893248 available bytes; 82.22% used; 112476531 free inodes.

server1 `/mnt/raid5`: 363948720128 available bytes; 98.33% used; 337545675 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23109509120 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23109509120 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23109509120 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23109509120 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 319793643520 available bytes; 97.79% used; 445072012 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84426657792 available bytes; 95.29% used; 114153471 free inodes.

server3 `/home`: 84426657792 available bytes; 95.29% used; 114153471 free inodes.

server3 `/data`: 142169907200 available bytes; 98.04% used; 225807596 free inodes.

server3 `/tmp`: 84426657792 available bytes; 95.29% used; 114153471 free inodes.

server3 `/var/tmp`: 84426657792 available bytes; 95.29% used; 114153471 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105637638144 available bytes; 94.11% used; 114349678 free inodes.

server4 `/home`: 105637638144 available bytes; 94.11% used; 114349678 free inodes.

server4 `/data`: 231349567488 available bytes; 96.80% used; 224943911 free inodes.

server4 `/tmp`: 105637638144 available bytes; 94.11% used; 114349678 free inodes.

server4 `/var/tmp`: 105637638144 available bytes; 94.11% used; 114349678 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
