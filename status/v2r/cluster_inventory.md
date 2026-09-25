# V2R cluster inventory

2026-09-25T10:25:39.978929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318836281344 available bytes; 82.21% used; 112480397 free inodes.

server1 `/home`: 318836281344 available bytes; 82.21% used; 112480397 free inodes.

server1 `/tmp`: 318836281344 available bytes; 82.21% used; 112480397 free inodes.

server1 `/var/tmp`: 318836281344 available bytes; 82.21% used; 112480397 free inodes.

server1 `/mnt/raid5`: 371140202496 available bytes; 98.30% used; 337555912 free inodes.
| server2 | True | ['3', '5', '6'] | [] |

server2 `/`: 22832267264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22832267264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22832267264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22832267264 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 316291915776 available bytes; 97.81% used; 445090869 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84416184320 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84416184320 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142021750784 available bytes; 98.04% used; 225815849 free inodes.

server3 `/tmp`: 84416184320 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84416184320 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105613512704 available bytes; 94.11% used; 114350253 free inodes.

server4 `/home`: 105613512704 available bytes; 94.11% used; 114350253 free inodes.

server4 `/data`: 238450282496 available bytes; 96.70% used; 224988141 free inodes.

server4 `/tmp`: 105613512704 available bytes; 94.11% used; 114350253 free inodes.

server4 `/var/tmp`: 105613512704 available bytes; 94.11% used; 114350253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
