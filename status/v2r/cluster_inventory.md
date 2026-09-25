# V2R cluster inventory

2026-09-25T08:53:39.889562+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318839877632 available bytes; 82.21% used; 112480391 free inodes.

server1 `/home`: 318839877632 available bytes; 82.21% used; 112480391 free inodes.

server1 `/tmp`: 318839877632 available bytes; 82.21% used; 112480391 free inodes.

server1 `/var/tmp`: 318839877632 available bytes; 82.21% used; 112480391 free inodes.

server1 `/mnt/raid5`: 364202672128 available bytes; 98.33% used; 337557016 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22831759360 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22831759360 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22831759360 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22831759360 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 332784369664 available bytes; 97.70% used; 445093562 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84437348352 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84437348352 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142375825408 available bytes; 98.03% used; 225811273 free inodes.

server3 `/tmp`: 84437348352 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84437348352 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105633288192 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633288192 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243401437184 available bytes; 96.64% used; 225000846 free inodes.

server4 `/tmp`: 105633288192 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633288192 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
