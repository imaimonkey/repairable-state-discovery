# V2R cluster inventory

2026-09-25T14:14:04.458388+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319152279552 available bytes; 82.20% used; 112476969 free inodes.

server1 `/home`: 319152279552 available bytes; 82.20% used; 112476969 free inodes.

server1 `/tmp`: 319152279552 available bytes; 82.20% used; 112476969 free inodes.

server1 `/var/tmp`: 319152279552 available bytes; 82.20% used; 112476969 free inodes.

server1 `/mnt/raid5`: 364069773312 available bytes; 98.33% used; 337547425 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4723036160 available bytes; 99.74% used; 110407465 free inodes.

server2 `/home`: 4723036160 available bytes; 99.74% used; 110407465 free inodes.

server2 `/tmp`: 4723036160 available bytes; 99.74% used; 110407465 free inodes.

server2 `/var/tmp`: 4723036160 available bytes; 99.74% used; 110407465 free inodes.

server2 `/mnt/raid5`: 321892851712 available bytes; 97.78% used; 445075903 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281991168 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84281991168 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142215045120 available bytes; 98.03% used; 225808959 free inodes.

server3 `/tmp`: 84281991168 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84281991168 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654755328 available bytes; 94.10% used; 114349705 free inodes.

server4 `/home`: 105654755328 available bytes; 94.10% used; 114349705 free inodes.

server4 `/data`: 231453024256 available bytes; 96.80% used; 224947283 free inodes.

server4 `/tmp`: 105654755328 available bytes; 94.10% used; 114349705 free inodes.

server4 `/var/tmp`: 105654755328 available bytes; 94.10% used; 114349705 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
