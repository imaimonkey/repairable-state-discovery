# V2R cluster inventory

2026-09-25T10:11:52.209443+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318834987008 available bytes; 82.21% used; 112480387 free inodes.

server1 `/home`: 318834987008 available bytes; 82.21% used; 112480387 free inodes.

server1 `/tmp`: 318834987008 available bytes; 82.21% used; 112480387 free inodes.

server1 `/var/tmp`: 318834987008 available bytes; 82.21% used; 112480387 free inodes.

server1 `/mnt/raid5`: 364874674176 available bytes; 98.33% used; 337556407 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22827147264 available bytes; 98.73% used; 110410476 free inodes.

server2 `/home`: 22827147264 available bytes; 98.73% used; 110410476 free inodes.

server2 `/tmp`: 22827147264 available bytes; 98.73% used; 110410476 free inodes.

server2 `/var/tmp`: 22827147264 available bytes; 98.73% used; 110410476 free inodes.

server2 `/mnt/raid5`: 316160045056 available bytes; 97.82% used; 445091057 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84417753088 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84417753088 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142027153408 available bytes; 98.04% used; 225816226 free inodes.

server3 `/tmp`: 84417753088 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84417753088 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614045184 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614045184 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240077787136 available bytes; 96.68% used; 224989761 free inodes.

server4 `/tmp`: 105614045184 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614045184 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
